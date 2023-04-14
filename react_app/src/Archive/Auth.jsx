import axios from "axios";


const axiosService = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    headers: { "Content-Type": "application/json", },
  });



function getUserInfo() {
    const auth = JSON.parse(localStorage.getItem("auth")) || null;
    const data = {
        id: auth.id,
        email: auth.email,
        password: auth.password,
    }
    return axios
      .post(`http://127.0.0.1:8000/api/users/${auth.id}/`, data)
      .then((res) => { 
        console.log(res)
         })
  }




export {
    getUser,
    getUserInfo,
}