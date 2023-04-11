import axios from "axios";
// import { useNavigate } from "react-router-dom";

function useUserActions() {
    // const navigate = useNavigate();
    const baseURL = "http://localhost:8000/api";

    const axiosService = axios.create({
        baseURL: baseURL,
        headers: {"Content-Type": "application/json", "Access-Control-Allow-Methods": "GET, PUT, POST, DELETE"},
        timeout: 1000,
    });
    
    return {
        getAllIdeas,
        getIm,


    }

    function getIm() {
        if (localStorage.getItem('im')){
            return localStorage.getItem('im')
        } else if (localStorage.getItem('auth')) {
            const auth = localStorage.getItem('auth')
            axios.get(`users/${auth.id}`)
            .then( res => {
                console.log('res.data.results')
                console.log(res.data.results)
                return res.data.results
                } )
            .catch((err) => {
                    if (err.message) {console.log(err);}
                    });
        } else {
            return []
        }
    }

    function getAllIdeas(){
        return axiosService.post('ideas').then((res) => res.data.results)
        }
    
    

    function login(data) {
        return axios.post(`${baseURL}/auth/login/`,
        data).then((res) => {
        // setUserData(data);
        // navigate("/");
        });
    }

    function logout() {
        localStorage.removeItem("auth");
        // navigate("/login");
    }


    function getUser() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth.user;
    }

    function getAccessToken() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth.access;
    }

    function getRefreshToken() {
        const auth = JSON.parse(localStorage.getItem("auth"));
        return auth.refresh;
    }

    // function setUserData(data) {
    //     localStorage.setItem("auth", 
    //         JSON.stringify({
    //             access: res.data.access,
    //             refresh: res.data.refresh,
    //             user: res.data.user,
    //             })
    //     );
    // }
    function edit(data, userId) {
        return axiosService.patch(`${baseURL}/user/${userId}/`,
        data).then((res) => {
        localStorage.setItem("auth",
            JSON.stringify({
                access: getAccessToken(),
                refresh: getRefreshToken(),
                user: res.data,})
                );
        });
    }
}

export {
    useUserActions,

};