<template>
    <body>
        <div class="container" id="container">
            <div class="form-container sign-in">
                <form @submit.prevent="handleAdminLogin">
                    <h1>Sign In</h1>
                    <input type="text" v-model="username" placeholder="Username">
                    <input id="password" :type="showPassword ? 'text' : 'password'" v-model="password" placeholder="Password">
                    <label><input id="showpassword" type="checkbox" v-model="showPassword" /> Show Password</label>
                    <button type="submit">Sign In</button>
                </form>
            </div>

            <!-- For toggling back and forth -->
            <div class="toggle-container">
                <div class="toggle">
                    <div class="toggle-panel toggle-left">
                        <h1>Welcome Back!</h1>
                        <p>Click to sign in if you already have an account!</p>
                        <button class="hidden" id="login">Sign In</button>
                    </div>
                    <div class="toggle-panel toggle-right">
                        <h1>Hello, welcome!</h1>
                        <p>Not an Administrator?</p>
                        <a href="/">
                            <button class="hidden">Student Login</button>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </body>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: '',
            baseUrl: 'https://kw3vt7l4jk.execute-api.us-east-1.amazonaws.com/Prod',
            showPassword: false
        };
    },
    methods: {
        // function to handle login functionality
        async handleAdminLogin() {
            try {
                // get data from login form
                const requestData = {
                    httpMethod: 'POST',
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password
                    }),
                };
                
                // await response from api gateway / lambda function
                const response = await fetch(this.baseUrl + '/adminlogin', {
                    method: 'POST',
                    mode: 'cors',
                    body: JSON.stringify(requestData),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                // respond accordingly
                const responseBody = await response.json();
                const rep = JSON.parse(JSON.stringify(responseBody));
                if (rep.statusCode == 200) {
                    this.$loggedin = true;
                    this.$router.push({name: 'AdminHome'});

                } else {
                    window.alert(rep.body);
                }

            } catch (error) {
                console.error('Error:', error);
                window.alert('Error: Login failed' + error + "   " + this.baseUrl + '/adminlogin');
            }
        }
    }
};

</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
}

body{
    background-color: #c9d6ff;
    background: linear-gradient(to right, #e2e2e2, #c9d6ff);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 100vh;
}

label {
    display: block;
    padding-left: 15px;
    text-indent: -15px;
    font-size: 14px;
}

#showpassword {
    width: 13px;
    height: 13px;
    padding: 0;
    margin:0;
    vertical-align: bottom;
    position: relative;
    top: -1px;
}
.container{
    background-color: #fff;
    border-radius: 30px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
}

.container p{
    font-size: 14px;
    line-height: 20px;
    letter-spacing: 0.3px;
    margin: 20px 0;
}

.container span{
    font-size: 12px;
}

.container a{
    color: #333;
    font-size: 13px;
    text-decoration: none;
    margin: 15px 0 10px;
}

.container button{
    background-color: #9e2d2d;
    color: #fff;
    font-size: 12px;
    padding: 10px 45px;
    border: 1px solid transparent;
    border-radius: 8px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-top: 10px;
    cursor: pointer;
}

.container button.hidden{
    background-color: transparent;
    border-color: #fff;
}

.container form{
    background-color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 40px;
    height: 100%;
}

.container input{
    background-color: #eee;
    border: none;
    margin: 8px 0;
    padding: 10px 15px;
    font-size: 13px;
    border-radius: 8px;
    width: 100%;
    outline: none;
}

.form-container{
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
}

.sign-in{
    left: 0;
    width: 50%;
    z-index: 2;
}

.container.active .sign-in{
    transform: translateX(100%);
}

.sign-up{
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;
}

.container.active .sign-up{
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: move 0.6s;
}

@keyframes move{
    0%, 49.99%{
        opacity: 0;
        z-index: 1;
    }
    50%, 100%{
        opacity: 1;
        z-index: 5;
    }
}

.toggle-container{
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: all 0.65s ease-in-out;
    border-radius: 150px 0 0 100px;
    z-index: 1000;
}

.container.active .toggle-container{
    transform: translateX(-100%);
    border-radius: 0 150px 100px 0;
}

.toggle{
    background-color: #2da82d;
    height: 100%;
    background: linear-gradient(to right, hsl(340, 83%, 76%), #690d0d);
    color: #fff;
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    transform: translateX(0);
    transition: all 0.6s ease-in-out;
}

.container.active .toggle{
    transform: translateX(50%);
}

.toggle-panel{
    position: absolute;
    width: 50%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 30px;
    text-align: center;
    top: 0;
    transform: translateX(0);
    transition: all 0.6s ease-in-out;
}

.toggle-left{
    transform: translateX(-200%);
}

.container.active .toggle-left{
    transform: translateX(0);
}

.toggle-right{
    right: 0;
    transform: translateX(0);
}

.container.active .toggle-right{
    transform: translateX(200%);
}
</style>