### Getting Started with Kueue Jobs

Hello\! This guide will help you build your own Docker container and run a Kueue job using the provided files.

Choose whether you want to run `CPU` based jobs or `GPU` based jobs, then go into the specific folder.

#### 1\. Build the Docker Container

First, you'll need to build the Docker image for your job.

1.  Navigate to the `container` folder. This is where your `Dockerfile` and `*test.py` files are located.

2.  Open a terminal in this folder and run the following command to build the image:

    ```sh
    docker build -t your-username/tf-test:cpu .
    ```

    Make sure to replace `your-username` with your actual Docker Hub username.

3.  After the build is complete, push the image to your Docker Hub repository:

    ```sh
    docker push your-username/tf-test:cpu
    ```

#### 2\. Update the Job Configuration

Now, let's configure your job to use the new image.

1.  Open the `job-ns-a.yaml` file.
2.  Find the `image` field under the `containers` section.
3.  Change the image name to the one you just pushed to Docker Hub. It should look like this:
    ```yaml
    containers:
      - name: tf-cpu-job
        image: your-username/tf-test:cpu
        # ... other configurations
    ```

Note: Make sure you have access to docker repo in your K8 cluster. If not you can create a secret with your docker login credentials. Refer this [document](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/) for more.

Replace your secret in `imagePullSecrets` field.

#### 3\. Run the Kueue Job

You're all set\! Now you can create the Kueue objects and your job in your Kubernetes cluster.

1.  Apply the ResourceFlavor and ClusterQueue first:

    ```sh
    kubectl apply -f resource_flavor.yaml
    kubectl apply -f cluster-queue.yaml
    ```

2.  Next, create the LocalQueue:

    ```sh
    kubectl apply -f local-queue.yaml
    ```

3.  Finally, create your job. Kueue will take care of scheduling and running it for you\!

    ```sh
    kubectl apply -f job-ns-a.yaml
    ```

You can check the status of your job with `kubectl get jobs -n kueue-jobs-ns-a`.

You can also schedule multiple jobs. Run the script, provide the time between new jobs popping up. Here I provide 10 seconds.

```sh
$ chmod +x ./run_workloads,sh
$ ./run_workloads.sh jobs-ns-a.yaml 10
```

This will schedule jobs every 10 seconds.

Happy job running\!
