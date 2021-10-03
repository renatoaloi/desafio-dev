import React from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "react-query";
import Home from "./pages/Home";
import Stores from "./pages/Stores";
import Upload from "./pages/Upload";
import "./App.css";

const queryClient = new QueryClient();

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <header className="header">
          <div className="title">
            <img
              src="1200px-Cog_font_awesome.svg.png"
              alt="CNAB Parser's logo"
              className="logo"
            />
            <h1>CNAB Parser Application</h1>
          </div>
          <div>
            <nav>
              <ul className="menu">
                <li>
                  <Link to="/">Home</Link>
                </li>
                <li>
                  <Link to="/upload">Upload CNAB</Link>
                </li>
                <li>
                  <Link to="/lojas">Lojas</Link>
                </li>
              </ul>
            </nav>
          </div>
        </header>
        <Switch>
          <Route path="/lojas">
            <Stores />
          </Route>
          <Route path="/upload">
            <Upload />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </Router>
    </QueryClientProvider>
  );
}
