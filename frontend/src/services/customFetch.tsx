import {
    isConnectedStore,
    IsConnectedStoreInterface,
} from "@/hooks/isConnected";

const { fetch: originalFetch } = window;

window.fetch = async (
    ...args: Parameters<typeof originalFetch>
): Promise<Response> => {
    const { setIsConnected } = isConnectedStore() as IsConnectedStoreInterface;
    let [resource, config] = args;
    // request interceptor here

    // Ensure config is an object to prevent errors
    if (!config || typeof config !== "object") {
        config = {};
    }

    const response = await originalFetch(resource, config);
    if (response.status === 302) {
        setIsConnected(false);
    }
    // response interceptor here
    return response;
};
