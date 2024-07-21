# Stocknota
- lock python requirements `bazelisk run //:requirements.update`

## Development setup
```bash
bazelisk run //:requirements.update
bash .vscode/setup_virtual.sh # For vscode interpreter

ibazel run projects/app:run
bazelisk run projects/app:tarball && docker run --rm gcr.io/stocknota_app:latest
```