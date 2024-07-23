# Stocknota
- lock python requirements `bazelisk run //:requirements.update`

## Development setup
```bash
bazelisk run //:requirements.update
bazelisk run projects/app:run # bazel-out/k8-fastbuild/bin/projects/app/run.runfiles/.run.venv will be created. Use the python as intepreter


ibazel run projects/app:run
bazelisk run projects/app:tarball && docker run --rm gcr.io/stocknota_app:latest
```