import { create } from "zustand";

export interface IsConnectedStoreInterface {
    isConnected: boolean;
    setIsConnected: (connectingState: boolean) => void;
}

export interface isConnectedSStoreInterface {
    isConnectedS: boolean;
    setIsConnectedS: (value: boolean) => void;
}

export const isConnectedStore = create((set) => ({
    isConnected: "bg-white",
    setIsConnected: (connectionStatus: string) =>
        set({ isConnected: connectionStatus }),
}));
