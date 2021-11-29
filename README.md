# resal-project
This repo contain an assignment project that was part of junior software engineer job interview at [Resal](https://resal.zohorecruit.com/jobs/Careers/595124000001006030/Junior-Software-Engineer?source=CareerSite)


the assignment :
```
There are two steps included. You will have 5 days to submit your work. 
You don’t have to finish all steps, it’s more important to complete each step properly.

1. You will use python to develop an API with an endpoint that accepts a CSV file and
    return a JSON file. Sample input and output are as follows:

Input:

id,product_name,customer_average_rating
132,"Massoub gift card", 5.0
154,"Kebdah gift card", 3.2
12,"Fatayer gift card", 1.8

Output:

{
    "top_product": "Massoub gift card",
    "product_rating": 5.0
}

To complete this step, we highly recommend using this project generator: 
https://fastapi.tiangolo.com/project-generation/#full-stack-fastapi-postgresql

It goes without saying that we expect you to implement unit tests and all other software engineering practices.

2. At this step, we will assume that Step 1 endpoint is going to take a long time to return a response and that will
    timeout the request. To avoid that, we need to implement a message-based solution. 
If you don’t have time to implement it, you can write a paragraph explaining how would you resolve this issue.
```
