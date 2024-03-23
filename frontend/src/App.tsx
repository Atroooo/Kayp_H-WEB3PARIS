import './App.css'
import {Routes, Route, BrowserRouter } from "react-router-dom";
import ProtectedRoute from "@/hooks/ProtectedRoute.tsx";
import Sidebar2 from "@/components/Sidebar.tsx";

function App() {

    const isConnected = true;

    console.log("isConnected: " + isConnected);
      return (
          <>
              <BrowserRouter>
                  <Routes>
                      <Route path="/sign-in" element={
                          <ProtectedRoute isAllowed={!isConnected} redirectPath={'/'}>
                              <div>Sign-in</div>
                          </ProtectedRoute>}>
                      </Route>

                      <Route>
                          <Route path="/" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>Dashboard</div>
                              </ProtectedRoute>}>
                          </Route>

                          <Route path="/bol/create" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>Create new document</div>
                              </ProtectedRoute>}>
                          </Route>

                          <Route path="/bol/list" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>List of documents</div>
                              </ProtectedRoute>}>
                          </Route>

                          <Route path="/bol/draft" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>Draft</div>
                              </ProtectedRoute>}>
                          </Route>

                          <Route path="/activity/notifications" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>Notifications</div>
                              </ProtectedRoute>}>
                          </Route>

                          <Route path="/activity/history" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>History</div>
                              </ProtectedRoute>}>
                          </Route>

                          <Route path="/settings" element={
                              <ProtectedRoute isAllowed={isConnected} redirectPath={"/sign-in"}>
                                  <Sidebar2 />
                                  <div>Settings</div>
                              </ProtectedRoute>}>
                          </Route>
                      </Route>

                  </Routes>
              </BrowserRouter>
          </>
      )
}


export default App
