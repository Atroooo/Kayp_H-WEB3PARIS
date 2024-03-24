import { create } from "zustand";

export interface IsConnectedStoreInterface {
    isConnected: boolean;
    setIsConnected: (connectingState: boolean) => void;
}

export const isConnectedStore = create((set) => ({
    isConnected: true,
    setIsConnected: (connectingState: string) =>
        set({ isConnected: connectingState }),
}));
