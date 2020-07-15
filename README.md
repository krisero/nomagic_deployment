Local vagrant environment:

```cd local_env; vagrant up ```

Setup environment before deployment:

```ansible-playbook -i hosts setup.yml --ask-vault-pass```

Deploy website:

```ansible-playbook -i hosts deployment.yml --ask-vault-pass```

*password is like company name with lowercase


Tests:

1. For each role in directory ```nomagic_deployment/roles/<ROLE_NAME>/molecule/default/``` create ```vault.pw``` with raw password 

2. For each role run in role directory ```molecule test```