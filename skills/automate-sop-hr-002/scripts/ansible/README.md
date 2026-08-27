# Hire for an open role: requisition to signed contract — Ansible

Idempotent role generated from the SOP. Automatable steps are tasks; manual steps are `pause` checkpoints; destructive steps are gated behind `confirm_destructive`.

```bash
ansible-playbook -i inventory.ini playbook.yml --check   # dry run
ansible-playbook -i inventory.ini playbook.yml --tags S3       # one step
ansible-playbook -i inventory.ini playbook.yml -e confirm_destructive=true
```

Search the tasks for `TODO` to finish the parts the IR left abstract (real `changed_when`, `creates:`/`removes:` guards for idempotence).
