import axios from "axios";
import React, { useEffect, useState } from "react"
import { useNavigate } from "react-router-dom";

function MakeIdea() {
    const navigate = useNavigate();
    const [rubrics, setRubric] = useState([]);
    const [oneRubric, setOneRubric] = useState([]);
    const [error, setRubricError] = useState("");
    const [loaded, setRubricLoaded] = useState(false);

    useEffect(() => {
        axios
            .get('http://127.0.0.1:8000/api/rubrics/', {"Content-Type": "application/json", })
            .then((response) => setRubric(response.data.results))
            .catch((error) => setRubricError(error.message))
            .finally(() => setRubricLoaded(true))
        
        },[])

    function handleSubmit(e) {
        e.preventDefault();
        const loginForm = e.currentTarget;
        const form = new FormData();
        const user = JSON.parse(localStorage.getItem('auth'))
 

        form.append("user", user.user.id)
        form.append("title", loginForm.title.value)
        form.append("rubric", loginForm.rubrics.value)
        form.append("preview", loginForm.preview.value)
        form.append("body", loginForm.body.value)



        axios
            .post('http://127.0.0.1:8000/api/ideas/', form, {"Content-Type": "application/json", })
            .then(res =>  console.log(res.data))
            .catch((error) => alert.error(error.message))
            .finally(() => setRubricLoaded(true))
        navigate("/");

    }

    function changeHandler(event){
        setOneRubric(event.target.value)
    }


    return (
        <div className="container-md site-container">
        <div className="container-md mt-5">
            <div className="row justify-content-center align-items-top">
            <div className="col-8">
            <div className="mb-3">
                <form 
                    id="new_idea-form"
                    onSubmit={handleSubmit}
                    method="post">

                    <div className="container">

                        <div className="row justify-content-center align-items-center g-2">
                            
                            <div className="col-8">
                                <label className="form-label">Название идеи</label>
                                <input name="title" type="text" className="form-control" id="ideaName" placeholder="Название"/>
                            </div>

                            <div className="col">
                                <label className="form-label">Рубрика</label>
                                <select className="form-select form-select" name="rubrics" onChange={changeHandler} id="rubrics">
                                    {rubrics.map(rubric => 

                                    <option key={rubric.id} value={rubric.id}>{rubric.rubirc}</option> )}
                                   
                                </select>
                            </div>
                        </div>

                        <div className="row justify-content-center align-items-center g-2">
                            <div className="col">
                                <label  className="form-label">Описание</label>
                                <textarea id='preview' name="preview" type="text" className="form-control"
                                    placeholder="Введите описание"></textarea>
                            </div>
                        </div>

                        <div className="row justify-content-center align-items-center g-2 mb-3">
                            <label  className="form-label">Содержание</label>
                            <textarea id='body' name="body" type="text" className="form-control"
                                placeholder="Введите содержание"></textarea>
                        </div>

                        <div className="row justify-content-center align-items-center ">
                                <button type="submit" className="btn mainButton">Добавить идею</button>
                        </div>

                    </div>
                </form>
                
            </div>
            </div>
            </div>
        </div>
    </div> 
    )


}
export default MakeIdea;