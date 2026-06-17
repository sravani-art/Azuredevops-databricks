name: notebook-migration-bundle 

# Mapping local source code to target workspace locations
artifacts:
  default:
    type: whl
    path: .

# Targets define destination environments
targets:
  dev:
    workspace:
      host: https://dbc-8bd766c2-3a5a.cloud.databricks.com # Replace with your Dev workspace URL
      root_path: /Shared/.bundle/${bundle.name}/dev


# Optional: Automatically deploy notebooks as a runnable asset
resources:
  jobs:
    sample_notebook_job:
      name: "[${bundle.target}] Sample Notebook Job"
      tasks:
        - task_key: run_notebook
          existing_cluster_id: c76a6fbe614c2943 # Replace with a valid cluster ID
          notebook_task:
            notebook_path: ../src/sample_notebook.py
