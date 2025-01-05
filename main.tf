terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

# -> main.tf <-

# Change docker provider as follows

provider "docker" {
host = "unix:///Users/andrewbecker/.docker/run/docker.sock"
}

resource "docker_image" "customer_api" {
  name         = "customer_api:testingtf"
  build {
    context    = "${path.module}/"
    dockerfile = "${path.module}/dockerfile"

    # Optionally specify build arguments
    tag = []
    # Use the target stage if necessary
    target = "test" # Specify the final stage name from your Dockerfile
    label = {author: "Andrew" }
  }

}


