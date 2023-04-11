import axios from "axios";




const axiosService = axios.create({
    baseURL: "http://localhost:8000/api/",
    timeout: 1000,
      
})

const config = {
    headers: {"Content-Type": "application/json" },
}

const getAll = () => {
    return axiosService.get('ideas')
}

function getAuth() {
    const auth = JSON.parse(localStorage.getItem("auth"))
    if (auth) {
        return auth
    } else {
        return null
    }
}


function getIdea(id) {
    const auth = JSON.parse(localStorage.getItem("auth"))
    if (auth) {
        config['Authorization'] = `Bearer ${auth.access}`
        return axiosService.get(`idea/${id}`, config)
    } else {
        return null
    }
}






export {
    getAll,
    getAuth,
    getIdea,


}