import { create } from "zustand";

export interface IsConnectedStoreInterface {
    isConnected: boolean;
    setIsConnected: (connectingState: boolean) => void;
}

export const isConnectedStore = create((set) => ({
    isConnected: false,
    setIsConnected: (connectingState: string) =>
        set({ isConnected: connectingState }),
}));
