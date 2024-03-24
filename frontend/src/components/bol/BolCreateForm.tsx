import { SubmitHandler, useForm} from "react-hook-form";
import {BillOfLading} from "@/types/BillOfLading.ts";
import { Input } from "../ui/input";
import { CardContent} from "@/components/ui/card.tsx";
import {Label} from "@/components/ui/label.tsx";
import {Button} from "@/components/ui/button.tsx";
import {Separator} from "@/components/ui/separator.tsx";
import {Calendar} from "@/components/ui/calendar.tsx";
import { format } from "date-fns"
import { Calendar as CalendarIcon, Flag, Map, Package, Ship} from "lucide-react"
import { cn } from "@/lib/utils"
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
} from "@/components/ui/popover"
import {useState} from "react";
import {Textarea} from "@/components/ui/textarea.tsx";
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import {commercialPorts} from "@/data/CommercialPorts.ts";
import {Link} from "react-router-dom";
import {createBol} from "@/services/bolService.ts";

const bol= {
    shipper: {
        name: "Shangan Automobiles",
        address: "10 Marsiling Rd Marsiling, Singapore"
    },
    consignee: {
        name: "Renault",
        address: "144 Friedrich Damm Hamburg, Deutschland"
    },
    cargo: {
        description: "Bananas",
        value: "150.000 $",
    },
    vesselDetails: {
        loadingPort: "",
        destinationPort: "",
    }
};

export function BolCreateForm() {
    const {
        handleSubmit,
        register,
    } = useForm<BillOfLading>({ defaultValues: bol})
    const onSubmit: SubmitHandler<BillOfLading> = (data) => console.log(data)

    return (
            <form onSubmit={handleSubmit(onSubmit)} className="h-full w-full">
                <CardContent className={"flex flex-col gap-7"}>
                    <div className={"grid grid-cols-2 gap-3 w-full"}>
                        <BolInputLayout title={"Shipper"} description={"add required shipper details"} icon={<Ship width={20}/>}>
                            <Label className={"text-left"}>Name</Label>
                            <Input type="text" placeholder="Name" {...register("shipper.name")} />
                            <Label className={"text-left"}>Address</Label>
                            <Input type="text" placeholder="Address" {...register("shipper.address")} />
                        </BolInputLayout>
                        <BolInputLayout title={"Consignee"} description={"add required consignee details"} icon={<Flag width={20} />}>
                            <Label className={"text-left"}>Name</Label>
                            <Input type="text" placeholder="Name" {...register("consignee.name")} />
                            <Label className={"text-left"}>Address</Label>
                            <Input type="text" placeholder="Address" {...register("consignee.address")} />
                        </BolInputLayout>
                    </div>
                    <Separator />
                    <div className={"grid grid-cols-2 gap-3 w-full"}>
                        <BolInputLayout title={"Cargo"} description={"add required cargo details"} icon={<Package width={20}/>}>
                            <Label className={"text-left"}>Name</Label>
                            <Input type="text" placeholder="Description" {...register("cargo.description")} /><Label className={"text-left"}>Value</Label>
                            <Input type="text" placeholder="Value" {...register("cargo.value")} />
                        </BolInputLayout>
                        <BolInputLayout title={"Vessels"} description={"add required vessels details"} icon={<Map width={20} /> }>
                            <Label className={"text-left"}>Loading Port</Label>
                            <CommercialPortSelect defaultValue={commercialPorts[1]} />
                            <Label className={"text-left"}>Destination Port</Label>
                            <CommercialPortSelect defaultValue={commercialPorts[11]}/>
                            <Label className={"text-left"}>Date of loading</Label>
                            <BolDatePicker />
                        </BolInputLayout>
                    </div>
                    <Separator />
                    <BolInputLayout title={"Additional information"}>
                        <Textarea />
                    </BolInputLayout>
                    <Button onClick={() => createBol(bol)}>Emit bill of lading</Button>

                    <Link to={"/bol/success"}>
                        <Button onClick={() => createBol(bol)}>Emit bill of lading</Button>
                    </Link>
                </CardContent>
            </form>
    )
}

export function BolInputLayout({children, title, description, icon }: {
    children: React.ReactNode,
    title: string,
    description?: string
    icon?: React.ReactElement
}) {
    return (
        <div className="flex flex-col space-y-2 gap-1">
            <div>
                <div className={"flex gap-1.5"}>
                    {icon}
                    <h3 className="text-lg font-semibold text-left">{title}</h3>
                </div>
                <p className="text-sm text-gray-500 text-left">{description}</p>
            </div>
            <div className={"flex flex-col gap-1.5"}>
                {children}
            </div>
        </div>
    )
}

export function BolDatePicker() {
    const [date, setDate] = useState<Date>()

    return (
        <Popover>
            <PopoverTrigger asChild>
                <Button
                    variant={"outline"}
                    className={cn(
                        "justify-start text-left font-normal",
                        !date && "text-muted-foreground"
                    )}
                >
                    <CalendarIcon className="mr-2 h-4 w-4" />
                    {date ? format(date, "PPP") : <span>Pick a date</span>}
                </Button>
            </PopoverTrigger>
            <PopoverContent className="w-auto p-0">
                <Calendar
                    mode="single"
                    selected={date}
                    onSelect={setDate}
                    initialFocus
                />
            </PopoverContent>
        </Popover>
    )
}

export function CommercialPortSelect({ defaultValue }: {defaultValue?: string}) {
    return (
        <Select defaultValue={defaultValue}>
            <SelectTrigger>
                <SelectValue />
            </SelectTrigger>
            <SelectContent>
                <SelectGroup>
                    {commercialPorts.map((port) => (
                        <SelectItem key={port} value={port}>
                            {port}
                        </SelectItem>
                    ))}
                </SelectGroup>
            </SelectContent>
        </Select>
    )
}