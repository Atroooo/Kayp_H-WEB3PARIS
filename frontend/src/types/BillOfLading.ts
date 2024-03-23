import {z} from "zod";

type Shipper = {
    name: string;
    address: string;
    contact: string;
};

type Consignee = {
    name: string;
    address: string;
    contact: string;
};

type Cargo = {
    description: string;
    quantity: number;
    weight: number;
    volume: number;
    value: number;
};

type VesselDetails = {
    name: string;
    loadingPort: string;
    destinationPort: string;
    dateOfLoading: Date;
};

type BillOfLading = {
    shipper: Shipper;
    consignee: Consignee;
    cargo: Cargo;
    billOfLadingNumber: string;
    termsOfDelivery: string;
    vesselDetails: VesselDetails;
    carrierSignature: string;
    specialInstructions: string;
};

const ShipperSchema = z.object({
    name: z.string(),
    address: z.string(),
    contact: z.string()
});

const ConsigneeSchema = z.object({
    name: z.string(),
    address: z.string(),
    contact: z.string()
});

const CargoSchema = z.object({
    description: z.string(),
    quantity: z.number(),
    weight: z.number(),
    volume: z.number(),
    value: z.number()
});

const VesselDetailsSchema = z.object({
    name: z.string(),
    loadingPort: z.string(),
    destinationPort: z.string(),
    dateOfLoading: z.date()
});

// Schéma pour le Bill of Lading
const BillOfLadingSchema = z.object({
    shipper: ShipperSchema,
    consignee: ConsigneeSchema,
    cargo: CargoSchema,
    billOfLadingNumber: z.string(),
    termsOfDelivery: z.string(),
    vesselDetails: VesselDetailsSchema,
    carrierSignature: z.string(),
    specialInstructions: z.string()
});


export { BillOfLadingSchema };
export type { BillOfLading };