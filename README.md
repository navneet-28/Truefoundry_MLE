**About the Company**

**Motivation**

90% of ML Models don’t end up in Production! It takes most companies anywhere from 2-3 months for those that do. Compare this to the 15 minutes it takes teams on Facebook to deploy a model. Half of these models deployed by most companies break because of scaling issues. A good % of the remaining is discarded due to issues that can’t be detected because of the absence of the right monitoring and Observability Systems!

**What do we do?**

At TrueFoundry, we want to automate the parts in the ML pipeline that can be automated and empower Data Scientists and ML Engineers to be able to test models in production and iterate fast with as few dependencies on other teams as possible. We draw our motivation from products created by Platform teams in top tech companies like Facebook, Google, and Netflix, which allow all teams to move much faster and deploy and iterate on their own!

Our Workflow stores provide a structure to Data Scientist's code, makes it production ready and deploys model APIs with auto scaling enabled, monitoring and observability dashboards, business user facing demos - automatically.

Basically, you can go from Model to Live in 15 minutes with the best Practices!

**Mission**

Our mission is to make Machine Learning productionisation and monitoring simpler for anyone. Developers (SEs, ML Engineers, DSs) should just focus on writing the business logic at very high iteration speeds and everything else should be abstracted out from them!

**Vision**

Imagine a flow where after writing the code — you can call a genie and tell about your requirements like kind of service (Serverless, CronJob, Database, an API service), resource requirements like CPU, memory, etc and the genie creates the service with the best practices like Gitops, Infrastructure as Code (IAC) and then shows a dashboard with all the metrics created.

**ML Intern Assignment**

**HuggingFace Model Deployment**

## <a name="_s3og1rsf6m8x"></a>Background:

- Truefoundry currently supports deploying hugging face models directly with just a few clicks.
- When the model is deployed (you need to get access to the platform [1] and deploy the model on our platform [2]) the API endpoints are exposed with V2 Inference Protocol. This is because we are using [seldon’s mlserver](https://github.com/SeldonIO/MLServer) internally to deploy the model.
  You can read about V2 inference protocol [here.](https://docs.seldon.io/projects/seldon-core/en/latest/reference/apis/v2-protocol.html)
- The problem with V2 protocol is that it is difficult to understand and non intuitive to the user. So we want to improve this user experience.

## <a name="_m380y94ghcmv"></a>Goal:

- The goal of this assignment is to write a fastapi service, which takes input for the model (in the same format as the inference endpoints API of huggingface models on the huggingface hub website) and internally converts the input to V2 inference protocol and returns the response.

- Since the input format will be different for different huggingface pipeline, you should expose the final API as:

**POST https://<your-service-endpoint>/predict/**

with body as

****{

`    `"hf_pipeline": string,

`    `"model_deployed_url": string,

`    `"inputs": any,

`    `"parameters": {...}

}

****
where:

- hf_pipeline is the huggingface pipeline name like _text-classification_
- model_deployed_url is the deployed endpoint of the hugging face model (that you will paste from truefoundry’s dashboard)
- inputs and parameters vary according to hf_pipeline - You can find the inference API format of hugging face here:

[https://huggingface.co/docs/inference-endpoints/supported_tasks](h)

## <a name="_56jj7wk1lziv"></a>Addition Information:

- You should support the following four huggingface pipelines. Also we have mentioned one model for each pipeline you can use for testing:

1. [sshleifer/tiny-gpt2](https://huggingface.co/sshleifer/tiny-gpt2) [text-generation]

Input Format for your service: <https://huggingface.co/docs/inference-endpoints/supported_tasks#text-generation>

{

`    `"hf_pipeline": "text-generation",

`    `"model_deployed_url": string,

`    `"inputs": string,

`    `"parameters": {

`         `// ... Any keyword arguments accepted by text-generation

`     `}

}



1. [typeform/distilbert-base-uncased-mnli](h) [zero-shot-classification]

Input Format for your service: [https://huggingface.co/docs/inference-endpoints/supported_tasks#zero-shot-classification]()

{

`    `"hf_pipeline": "zero-shot-classification",

`    `"model_deployed_url": string,

`    `"inputs": string,

`    `"parameters": {

`         `candidate_labels: string[],

`         `// ... Any keyword arguments accepted by zero-shot-classification

`     `}

}



1. [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all/tree/main) [token-classification]

Input Format for your service: [https://huggingface.co/docs/inference-endpoints/supported_tasks#token-classifiation](h)

{

`    `"hf_pipeline": "token-classification",

`    `"model_deployed_url": string,

`    `"inputs": string,

`    `"parameters": {

`         `// ... Any keyword arguments accepted by token-classification

`     `}

}



1. [TahaDouaji/detr-doc-table-detection](h) [object-detection]

Input Format for your service: <https://huggingface.co/docs/inference-endpoints/supported_tasks#object-detection>

{

`    `"hf_pipeline": "object-detection",

`    `"model_deployed_url": string,

`    `"inputs": string, // http url to image OR base64 encoded image bytes

`    `"parameters": {

`         `// ... Any keyword arguments accepted by object-detection

`     `}

}



- The model deployment on truefoundry uses seldon’s mlserver in the background. To understand the input format for each pipeline, you can refer to this file: [https://github.com/SeldonIO/MLServer/blob/master/runtimes/huggingface/mlserver_huggingface/metadata.py](h)

## <a name="_xgczp146oe3k"></a>Starter Template and Test Runner:

<https://gist.github.com/chiragjn/62d9b0612c5e05a09d62b1b956a6154a>

## <a name="_lkwefqc00fri"></a>Evaluation Points:

- Try to support as many different pipelines as possible (from the list shown above)
- Try to make your code modular and write it in a way that it can be extended to any other HuggingFace pipeline.
- Finally at the time of submission, submit a deployed link for any of the pipeline and that too hosted on truefoundry. Relevant link : [https://docs.truefoundry.com/docs/deploying-your-first-service](h)

For the host value in port section follow this format

https://<your-app-name>-<workspace-name>-<port>.demo1.truefoundry.com



The New Service form on UI can help you generate this value

`	`**References**

**[1] Getting Access to Truefoundry’s Platform:**

You need to signup on <https://app.truefoundry.com> and [**join**](https://join.slack.com/t/truefoundry/shared_invite/zt-1siovkugy-yJLZF2FPz7HQjNxmKMuZSg) the slack channel and message there to get access to resources that will be necessary for you to complete the assignment.

1. For getting access to a workspace, signup on <https://app.truefoundry.com>\*\* and personally message Parth Kathuria to get access to workspace
1. Once you get access, you can start working on the assignment. You can post your **doubts** related to using our platform/assignment on a **slack channel named _“ml-intern-assgn”_**

**NOTE:** You will be given the workspace access for 7 days. You have to complete and submit the assignment within this time. After that - the workspace will be deleted.\*\*

**[2] Deploying a hugging face model on truefoundry:**

Get access to <https://app.truefoundry.com> and resources by joining our slack channel as described above.

- Go to deployments -> Model -> New Deployment
- Select your workspace
- Select hugging face model hub and enter the its name as shown below:
- Configure the resources wisely [GPU is not required and should NOT be used for any model] and click on submit
- You can use the following values for requests and limits:

For text-generation, token-classification, zero-shot-classification

resources:
`  `cpu_limit: 0.1
`  `cpu_request: 0.1

`  `memory_request: 850
`  `memory_limit: 900
`  `ephemeral_storage_limit: 1000
`  `ephemeral_storage_request: 1000



For object-detection model

resources:
`  `cpu_limit: 0.1
`  `cpu_request: 0.1

`  `memory_request: 1300
`  `memory_limit: 1500
`  `ephemeral_storage_limit: 1000
`  `ephemeral_storage_request: 1000



- Your model should be live in a few minutes
- Reference Link: <https://docs.truefoundry.com/docs/model-deployment-1#huggingfacemodelhub>

##

## <a name="_ookz39g6weiv"></a><a name="_dwmdn8dqui7z"></a>**How to submit the project ?**

The project should be done in github and please send us the link to the github repository by filling out this form: [https://forms.gle/GFjibmvmT2tjgHWSA ](https://forms.gle/GFjibmvmT2tjgHWSA)

We will review your code and you will hear back from us if we are ready to move you to the next stage. Please try to write a proper README in your github repo so that it’s easy to understand how to run the code.
The final stage involves a technical interview wherein we will discuss your projects, review the application you made above and test some general problem solving skills.

Feel free to email at <parth@truefoundry.com> if you have any questions. Best of luck for the project!
