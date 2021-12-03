# The `kaggle-starter` Kedro starter

## Introduction

The code in this repository is meant to be a starting point for a general Kaggle competition. This is a very agnostic pipeline that only has one node for querying the Kaggle API. See below for more information on how to get started.

## Use

...

## FAQ

<details>
<summary style="font-weight: bold"> Why is Kedro saying "Failed to find the pipeline named '__default__'"? </summary>

By design, there is no default pipeline in this starter. To run the API query pipeline, run `kedro run --pipeline api_query`. 

When adding pipelines be sure to exclude `api_query` so you don't pull from the Kaggle dataset every time your `__default__` pipeline runs.

</details>

<details>
<summary style="font-weight: bold"> Why am I seeing KeyError: "Unable to find credentials KAGGLE_AUTH ..."? </summary>

You forgot to add your `credentials.yml`. Add a file to `conf/local/` with your username and Kaggle key in the following format:

```yaml
KAGGLE_AUTH:
  - <my_username>
  - <my_kaggle_key>
```

Be sure to never commit this file to Github! Your Kaggle key is a secret and should be protected.

</details>

<details>
<summary style="font-weight: bold"> What does "kedro.io.core.DataSetError: ('Failed to fetch data' ...)" mean? </summary>

You need to specify an `id` and `filename` in the `url` field of your `kaggle_api` catalog entry.

</details>
