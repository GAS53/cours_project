import axios from "axios";




const axiosService = axios.create({
    baseURL: "http://localhost:8000/api/",
    timeout: 1000,
      
})

function loadAuth() {
    return JSON.parse(localStorage.getItem("auth"))
}

function getConfig(is_auth=true){
    const config = {
        headers: {"Content-Type": "application/json" },}
    if (is_auth) {
        const auth = loadAuth()
        config['Authorization'] = `Bearer ${auth.access}`
    }
    return config
}


const getAll = () => {
    return axiosService.get('ideas')
}

function getAuth() {
    const auth = loadAuth()
    if (auth) {
        return auth
    } else {
        return null
    }
}


function getIdea(id) {
    return axiosService.get(`idea/${id}`, getConfig())
}

function connectToIdea(id) {
    const auth = loadAuth()
    const data = { 
        pk: id,
        user: auth.user.public_id }
        console.log('data')
        console.log(data)
    return axiosService.patch('join/', data, getConfig(true))
} 

function createRubric(form){
    return axiosService.post(`new_rubric/`, form, getConfig())
}

function getRubrics(form){
    return axiosService.get(`rubrics/`, form, getConfig())
}

export {
    getAll,
    getAuth,
    getIdea,
    connectToIdea,
    createRubric,
    getRubrics,


}