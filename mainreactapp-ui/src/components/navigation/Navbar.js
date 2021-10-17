import React, {useState, useEffect} from "react";
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from "axios";

function Navbar() {
    const [artworks, setWorks] = useState([])

    useEffect(() => {
        axios({
            method: 'GET',
            url: '127.0.0.1:8000/api/artworks/'
        }).then(response => {
            setWorks(response.data)
        })
    }, [])
    return (
        <div className="App">
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">Portrait for Soul</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                            data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
                            aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="#">О художнике</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Портфолио</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Цены</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#" tabIndex="-1"
                                   aria-disabled="true">Контакты</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#" tabIndex="-1"
                                   aria-disabled="true">Отзывы</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    );
}

export default Navbar;
