💂🏻‍♂️

A simple Azure Function to scrape and return text content of any url.

`https://<function-app-name>.azurewebsites.net/api/invoke_scrapper?url=<any-url-you-wish-to-scrape>`


**If you wish to deploy everything as is in this repo**

1. Create an Azure Function App with the name: `scrapper-func`
2. Download the publish profile from Azure Portal
3. Add a secret `AZURE_FUNCTIONAPP_PUBLISH_PROFILE` in your github repository and paste the content of publish profile as value of the secret
4. Push a commit to your repository.
5. If everything goes as planned, Voila!
6. Hit the url `https://scrapper-func.azurewebsites.net/api/invoke_scrapper?url=<replace-this-with-any-url-you-wish-to-scrape>`
7. If it's a success you should see a repsonse `{"status": 200, "content":<content-scrapped-from-your-url> }`

