**Inspect HOA backend challenge**

This is a simple flask repository with some endpoints and requires 
a few more endpoints.

It follows a simple MVP (model-view-presenter) architecture with an additional data layer(repository) to access the data.

The view layer should only contain flask specific logic

The presenter layer should contain all the business logic 

The model layer contains the business-models

Please fork this repository and add your solution to your new fork



The endpoints for users for this application already exist and follow the required architecture.

Please look at the code and following the same pattern, add an endpoint for the users where a user id is 
taken in the url and the endpoint returns the user with that user ID

Also, create a new `hoas.py` file in the view and presenter directories and create 
the endpoints which can get all the HOAs and add another HOA following the same pattern as the users endpoints

NOTE: The repositories and models for HOAs and users have been finished and should not require any change, if you do need to change it, 
feel free and let us know why you chose to change it. 



