# Terraform scaffold — Hire for an open role: requisition to signed contract

Runs the automatable steps of `SOP-HR-002` as ordered `null_resource` provisioners.

```bash
terraform init
terraform plan                              # preview
terraform apply                             # run non-destructive steps
terraform apply -var confirm_destructive=true   # include destructive steps
```

Manual and decision steps are listed as comments in `main.tf` — Terraform does not perform them. Fill the `TODO` commands where the IR had no concrete command.
