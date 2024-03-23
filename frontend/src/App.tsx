import { Routes, Route, BrowserRouter } from "react-router-dom";
import ProtectedRoute from "@/hooks/ProtectedRoute.tsx";
import Sidebar2 from "@/components/Sidebar.tsx";
import Login from "./views/Login";

import { create } from "zustand";
import { BolCreate } from "@/views/BolCreate.tsx";

export interface IsConnectedStoreInterface {
    isConnected: boolean;
    setIsConnected: (connectingState: boolean) => void;
}

export const isConnectedStore = create((set) => ({
    isConnected: true,
    setIsConnected: (connectingState: boolean) =>
        set({ isConnected: connectingState }),
}));

function App() {
    const { isConnected } = isConnectedStore() as IsConnectedStoreInterface;
    console.log("isConnected: " + isConnected);

    const loginFallback = "/log-in";
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route
                        path={loginFallback}
                        element={
                            <ProtectedRoute
                                isAllowed={!isConnected}
                                redirectPath={"/"}
                            >
                                <Login />
                            </ProtectedRoute>
                        }
                    ></Route>

                    <Route>
                        <Route
                            path="/"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Dashboard</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/create"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <BolCreate />
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/list"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>List of documents</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/bol/draft"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Draft</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/activity/notifications"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Notifications</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/activity/history"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>History</div>
                                </ProtectedRoute>
                            }
                        ></Route>

                        <Route
                            path="/settings"
                            element={
                                <ProtectedRoute
                                    isAllowed={isConnected}
                                    redirectPath={loginFallback}
                                >
                                    <Sidebar2 />
                                    <div>Settings</div>
                                </ProtectedRoute>
                            }
                        ></Route>
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default App;
