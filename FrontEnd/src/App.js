import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "./icons.js";
import ReportScreen from "./screens/ReportScreen";
import InicioScreen from "./screens/InicioScreen";
import "./style.css";

function App() {
  return (
    <Router>
      <Route path="/" exact component={ReportScreen} />
      <Route path="/ReportScreen/" exact component={ReportScreen} />
      <Route path="/InicioScreen/" exact component={InicioScreen} />
    </Router>
  );
}

export default App;
