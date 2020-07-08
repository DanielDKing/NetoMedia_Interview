pipeline {
  agent {
      docker { image 'python:3.7.2' } 
  }
  stages {
    stage('build') {
      steps {
        sh 'pip install --user -r ./app/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python ./app/unit_test.py'
      }   
    }
  }
}