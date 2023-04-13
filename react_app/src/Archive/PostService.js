import axios from "axios";



const axiosService = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/',
    timeout: 1000,
    headers: {"Content-Type": "application/json",},
  });
    
export async function getIdeas(){
    const res = await axiosService('ideas/')
    return res.data.results
}

axiosService.interceptors.request.use(async (config) => {
  const { access } = JSON.parse(localStorage.getItem("auth"));
  config.headers.Authorization = `Bearer ${access}`;
  return config;
  });


var fruit = {
    name: 'supreuser',
    scientificName: 'Musa'
    };
  
var { name, scientificName } = fruit;

axiosService.interceptors.response.use(
  (res) => Promise.resolve(res),
  (err) => Promise.reject(err),
  );

const refreshAuthLogic = async (failedRequest) => {
    const { refresh } = JSON.parse(localStorage.getItem("auth"));
    return axios
    .post("/refresh/", null, {
    baseURL: "http://localhost:8000",
    headers: { Authorization: `Bearer ${refresh}`,
    },
    })
    .then((resp) => {
    const { access, refresh } = resp.data;
    failedRequest.response.config.headers["Authorization"] = "Bearer " + access;
    localStorage.setItem("auth", JSON.stringify({access, refresh }));
    })
    .catch(() => {
      localStorage.removeItem("auth");
    });
    };



  // createAuthRefreshInterceptor(axiosService, refreshAuthLogic);

  export function fetcher(url) {
      return axiosService.get(url)
      .then((res) => res.data);
      }


export default axiosService;







// axiosService.interceptors.request.use(async (config) => {
//     const { access } = JSON.parse(localStorage.getItem("auth"));
//         config.headers.Authorization = `Bearer ${access}`;
//         return config;
//         });

// var fruit = {
//         name: 'Banana',
//         scientificName: 'Musa'
//         };

// var { name, scientificName } = fruit;

// const refreshAuthLogic = async (failedRequest) => {
//         const { refresh } =  JSON.parse(localStorage.getItem("auth"));
//         return axios
//         .post("/refresh/token/", null, {
//         baseURL: "http://localhost:8000",
//         headers: { Authorization: `Bearer ${refresh}`,},})
//         .then((resp) => { const { access, refresh } = resp.data;
//             failedRequest.response.config.headers[
//             "Authorization"] = "Bearer " + access;
//         localStorage.setItem("auth", JSON.stringify({access, refresh }));})
//         .catch(() => {localStorage.removeItem("auth");
//     });
//     };

// createAuthRefreshInterceptor(axiosService, refreshAuthLogic);
        
//     export function fetcher(url) {
//         return axiosService.get(url).then((res) => res.data);
//         }
    


