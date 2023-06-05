def updated(data_json):
    ## Developed by gusanoesc
    try:
        repository = data_json
        # print(repository)
    except:
        print("Error PR Updated")
    repository_name = repository['repository']['name']
    repository_link = repository['repository']['links']['html']['href']

    project_name = repository['repository']['project']['key']

    actor_name = repository['actor']['display_name']

    pull_request_title = repository['pullrequest']['title']
    pull_request_state = repository['pullrequest']['state']
    pull_request_source_branch = repository['pullrequest']['source']['branch']['name']
    pull_request_destination = repository['pullrequest']['destination']['branch']['name']
    pull_request_source_link = repository['pullrequest']['links']['html']['href']

    message = "\nRepository: "+repository_name+"\nProject Name: "+project_name+"\nAuthor: "+actor_name+" ✏️"+"\nPR Title: "+pull_request_title+" 📌"+"\nPR State: "+pull_request_state+"- UPDATED 🔵"+"\nPull request: "+pull_request_source_branch+" ➡️ "+pull_request_destination+"\nPR Link: "+pull_request_source_link
    return message