import axios from "axios";


const axiosService = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    headers: { "Content-Type": "application/json", },
  });

function getUser() {
    const auth = JSON.parse(localStorage.getItem("auth")) || null;
    if (auth) {
      return auth.user;
    } else {
      return null;
    }
  }

function getUserInfo() {
    const auth = JSON.parse(localStorage.getItem("auth")) || null;
    const data = {
        public_id: auth.public_id,
        email: auth.email,
        password: auth.password,
    }
    return axios
      .post(`http://127.0.0.1:8000/api/users/${auth.public_id}/`, data)
      .then((res) => { 
        console.log(res)
         })
  }




export {
    getUser,
    getUserInfo,
}