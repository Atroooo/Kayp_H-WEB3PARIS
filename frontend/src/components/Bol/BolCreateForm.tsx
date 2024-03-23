import { SubmitHandler, useForm} from "react-hook-form";
import {BillOfLading} from "@/types/BillOfLading.ts";
import { Input } from "../ui/input";
import { CardContent} from "@/components/ui/card.tsx";
import {Label} from "@/components/ui/label.tsx";

export function BolCreateForm() {
    const {
        handleSubmit,
        register,
    } = useForm<BillOfLading>()
    const onSubmit: SubmitHandler<BillOfLading> = (data) => console.log(data)

    return (
            <form onSubmit={handleSubmit(onSubmit)} className="w-2/3 space-y-6">
                <CardContent>
                    <BolInputLayout title={"Shipper"} description={"add required shipper details"}>
                        <Label className={"text-left"}>Name</Label>
                        <Input type="text" placeholder="Name" {...register("shipper.name")} />
                        <Label className={"text-left"}>Contact</Label>
                        <Input type="text" placeholder="Contact" {...register("shipper.contact")} />
                        <Label className={"text-left"}>Address</Label>
                        <Input type="text" placeholder="Address" {...register("shipper.address")} />
                    </BolInputLayout>
                </CardContent>
            </form>
    )
}

export function BolInputLayout({children, title, description }: { children: React.ReactNode, title: string, description: string }) {
    return (
        <div className="flex flex-col space-y-2 gap-1">
            <div>
                <h3 className="text-lg font-semibold text-left">{title}</h3>
                <p className="text-sm text-gray-500 text-left">{description}</p>
            </div>
            <div>
                {children}
            </div>
        </div>
    )
}