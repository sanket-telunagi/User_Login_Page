                        This is the CTD project to create a login page

===========================================================================================

flow - 

                        Home page
                            |
                ------------ ---------------
            login                        register
                |                             |
    - (user existing)                   - (create user)
        login and redirect to homepage     Take all the information and create user
                                           After creation of user redirect to home page
    - (new user)
        redirect to register page


@superuser - 

    username - CTD
    password - DJ_admin
    email - not given

@test users - 

    @test user 1
    username   - test_user_1
    password   - test@123

    @test user 2
    username   - test_user_2
    password   - test2@123

    @test user 3
    username   - test_user_3
    password   - test3@123
    email      - test_user_3@gmail.com
    First name - test3
    Last name  - test4

    @test user 4
    username   - test_user_4
    password   - test4@123
    email      - test_user_4@gmail.com
    First name - ....
    Last name  - ....

    @test user 5
    username   - test_user_5
    password   - test5@123
    email      - test_user_5@gmail.com
    First name - ....
    Last name  - ....

Design - Glass morph theme


# Problem 

1. I am cofused about login and login/ in urls.py of users app ass these both gives different results if i try to 'login/' it works fine but whe 'login' comes it gives error as login does not exists 