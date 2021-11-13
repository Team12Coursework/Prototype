import axios from 'axios';

class AuthService {
    login(user) {
        const params = new URLSearchParams();
        params.append('username', user.username);
        params.append('password', user.password);

        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }

        return axios.post('http://localhost:8000/api/user/login', params, config)
        .then(response => {
            if (response.data.access_token) {
                localStorage.setItem('user', JSON.stringify({
                    username: user.name,
                    accessToken: response.data.access_token
                }));
                return response.data;
            }
        });
    }

    logout() {
        localStorage.removeItem('user');
    }

    register(user) {
        return axios.put('http://localhost:8000/api/user/register', {
            username: user.username,
            password: user.password,
        });
    }
}

export default new AuthService();
