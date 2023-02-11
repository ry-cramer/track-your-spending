import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import CreateTransactionPage from "./CreateTransactionPage";
import { BrowserRouter as Router, Routes, Route, Link, Redirect} from "react-router-dom";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div>
            <Router>
                <Routes>
                    <Route path='/' element={<HomePage />} />
                    <Route path='/create' element={<CreateTransactionPage />} />
                </Routes>
            </Router>
        </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);