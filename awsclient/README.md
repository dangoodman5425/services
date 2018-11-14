# Amazon Web Services
Amazon Web Services consists of API wrappers for a variety of AWS services including S3, SQS, and Athena 

## Installing

### Remotely
```
export AWS_FOLDER=conductor_data_tools/services/amazonwebservices
pip install git+https://${GITHUB_TOKEN}:x-oauth-basic@github.com/Conductor/science.git#subdirectory="${AWS_FOLDER}"
```

### Locally
```
cd /path/to/science
git checkout master
git pull origin master
cd conductor_data_tools/services/amazonwebservices
pip install .
```
