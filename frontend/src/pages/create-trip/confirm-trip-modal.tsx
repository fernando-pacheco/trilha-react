import { Mail, PlaneTakeoff, User, X } from "lucide-react";
import { FormEvent } from "react";
import { Button } from "../../components/button";
// import { DateRange } from "react-day-picker";

interface ConfirmTripModalProps {
    closeConfirmTripModal: () => void
    createTrip: (event: FormEvent<HTMLFormElement>) => void
    destination: string
    setOwnerEmail: (email: string) => void
    setOwnerName: (name: string) => void
    // eventDate: DateRange | undefined
}


export function ConfirmTripModal({
    closeConfirmTripModal,
    createTrip,
    destination,
    setOwnerEmail,
    setOwnerName,
    // eventDate
}: ConfirmTripModalProps) {
    return (
        <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
            <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
                <div className="space-y-2">
                    <div className="flex items-center justify-between">
                        <h2 className="text-lg font-semibold">Confirmar criação de viagem</h2>
                        <button type="button" onClick={closeConfirmTripModal}>
                            <X className="size-5 text-zinc-400" />
                        </button>
                    </div>

                    <p className="text-sm text-zinc-400 text-left">
                        Para concluir a criação da viagem para <span className="font-semibold text-zinc-100">{destination}</span> nas datas de <span className="font-semibold text-zinc-100">{'eventDate'}</span> preencha seus dados abaixo:
                    </p>
                </div>
                <form onSubmit={createTrip} className="space-y-3" >
                    <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex items-center gap-2">
                        <User className=" text-zinc-400 size-5" />
                        <input
                            type="text"
                            name="nome"
                            placeholder="Seu nome completo"
                            className="bg-transparent text-lg placeholder-zinc-400 flex-1 outline-none"
                            onChange={event => setOwnerName(event.target.value)}
                            />
                    </div>
                    <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex items-center gap-2">
                        <Mail className=" text-zinc-400 size-5" />
                        <input
                            type="email"
                            name="email"
                            placeholder="Seu e-mail pessoal"
                            className="bg-transparent text-lg placeholder-zinc-400 flex-1 outline-none"
                            onChange={event => setOwnerEmail(event.target.value)}
                        />
                    </div>

                    <Button type="submit" variant="primary" size="full">
                        Confirmar criação da viagem
                        <PlaneTakeoff className="size-5" />
                    </Button>
                </form>
            </div>
        </div>
    )
}