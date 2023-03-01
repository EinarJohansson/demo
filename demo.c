#include <hiredis/hiredis.h>
#include <stdlib.h>
#include <stdio.h>

#define PORT 6379

int main(int argc, char const *argv[])
{
  redisContext *c = redisConnect("127.0.0.1", PORT);
  
  if (c != NULL && c->err)
  {
    printf("Error: %s\n", c->errstr);
    // handle error
  }
  else
  {
    printf("Connected to Redis\n");
  }

  redisReply *reply;
  reply = redisCommand(c, "SMEMBERS %s", "db");
  if (reply == NULL)
  {
    printf("FAIL\n");
    exit(EXIT_FAILURE);
  }

  printf("%d\n", reply->elements);

  redisReply **replies = reply->element;

  for (size_t i = 0; i < reply->elements; i++)
  {
    printf("%s\n", (int) replies[i]->str);
    
    redisReply *lol = redisCommand(c, "SMEMBERS %s", replies[i]->str);
    redisReply **idk = lol->element;

    for (size_t j = 0; j < lol->elements; j++)
    {
      printf("%s\n", idk[j]->str);
    }

    puts("");
  }

  freeReplyObject(reply);

  redisFree(c);

  return 0;
}
