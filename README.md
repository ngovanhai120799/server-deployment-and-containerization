# server-deployment-and-containerization

### Test your Endpoint
EXTERNAL-IP:` http://a4156c2db9b50418a82e819bcb6ae620-698760468.us-east-1.elb.amazonaws.com:80`

```commandline
EXPORT TOKEN=`curl -d '{"email":"testuser1\@gmail.com","password":"Abcd@1234"}' -H "Content-Type: application/json" -X POST http://af3b4d4b508aa4ee893efdc4d127a1a2-1316768652.us-east-1.elb.amazonaws.com:80/auth  | jq -r '.token'`
curl --request GET 'http://af3b4d4b508aa4ee893efdc4d127a1a2-1316768652.us-east-1.elb.amazonaws.com:80/contents' -H "Authorization: Bearer ${TOKEN}" | jq 
```