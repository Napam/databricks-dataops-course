# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. Connect to serverless compute. Run through the cells
# MAGIC 3. Run the cells for deploying and running the dev job

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Workflows
# MAGIC
# MAGIC Workflows is on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A job is basically a recipe for some proceedures, a tasklist basically.
# MAGIC
# MAGIC A job-run is an execution of a "recipe". You can execute the same jobs multiple times.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC Write answer in the empty cell below.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC acme_transport_taxinyc_prep_dev_naphat_featgh141neovim_4c6799ab
# MAGIC
# MAGIC so the structure is
# MAGIC
# MAGIC [orgname].[department].[project].[flow].[env].[user].[jobid]
