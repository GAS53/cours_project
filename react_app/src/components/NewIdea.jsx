
import React, { useRef, useState } from "react";
import axios from "axios";

function NewIdea(props) { 
    const [rubric, setRubric] = useState()
    const titleInputRef = useRef();
    const previewInputRef = useRef();
    const bodyInputRef = useRef();
 

    function handleSubmit(e){
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        console.log('formData')
        const autor_id = JSON.parse(localStorage.getItem('auth'))
        console.log(autor_id)
        formData.append('autor_id', autor_id.user.public_id)
        console.log(formData)
        fetch('http://127.0.0.1:8000/api/ideas/', { method: form.method, body: formData });
        // You can generate a URL out of it, as the browser does by default:
        console.log(new URLSearchParams(formData).toString());
        // You can work with it as a plain object.
        const formJson = Object.fromEntries(formData.entries());
        console.log(formJson); // (!) This doesn't include multiple select values
        // Or you can get an array of name-value pairs.
        console.log([...formData.entries()]);
        
       
    
    
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
                        method="post"
                        >

                        <div className="container">

                            <div className="row justify-content-center align-items-center g-2">
                                
                                <div className="col-8">
                                    <label className="form-label">Название идеи</label>
                                    <input name="title" ref={titleInputRef} type="text" className="form-control" id="ideaName" placeholder="Название"/>
                                </div>

                                <div className="col">
                                    <label className="form-label">Рубрика</label>
                                    <select className="form-select form-select" name="rubrics" onChange={e => { setRubric(e)}} id="">
                                        <option selected value="Python">Python</option>
                                        <option value="JS">JS</option>
                                        <option value="Ещё что-то">Ещё что-то</option>
                                    </select>
                                </div>
                            </div>

                            <div className="row justify-content-center align-items-center g-2">
                                <div className="col">
                                    <label  className="form-label">Описание</label>
                                    <textarea name="preview"  ref={previewInputRef} type="text" className="form-control" id="preview"
                                        placeholder="Введите описание"></textarea>
                                </div>
                            </div>

                            <div className="row justify-content-center align-items-center g-2 mb-3">
                                <label  className="form-label">Содержание</label>
                                <textarea name="body" ref={bodyInputRef} type="text" className="form-control" id="preview"
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
)};


export default NewIdea