import { Calendar, CircleCheckBig, Clock, Tag, X } from "lucide-react"
import { Button } from "../../components/button"
import { FormEvent } from "react"
import { api } from "../../lib/axios"
import { useParams } from "react-router-dom"

interface CreateActivityModalProps {
    closeCreateActivityModal: () => void
}

export function CreateActivityModal({
    closeCreateActivityModal
}: CreateActivityModalProps) {
    const { tripId } = useParams()

    async function createActivity(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
        const data = new FormData(event.currentTarget)
        const title = data.get('title')
        const occurs_at = `${data.get('date')}T${data.get('time')}`

        await api.post(`/trips/${tripId}/activities/`, {
            title: title,
            occurs_at: occurs_at,
            trip: tripId
        })

        window.document.location.reload()
    }

    return (
        <div className="fixed inset-0 bg-black/60 flex items-center justify-center">
            <div className="w-[640px] rounded-xl py-5 px-6 shadow-shape bg-zinc-900 space-y-5">
                <div className="space-y-2">
                    <div className="flex items-center justify-between">
                        <h2 className="text-lg font-semibold">Cadastrar atividade</h2>
                        <button type="button" onClick={closeCreateActivityModal}>
                            <X className="size-5 text-zinc-400" />
                        </button>
                    </div>

                    <p className="text-sm text-zinc-400 text-left">
                        Todos os convidados podem ver as atividades
                    </p>
                </div>

                <form onSubmit={createActivity} className="space-y-3">
                    <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex items-center gap-2">
                        <Tag className=" text-zinc-400 size-5" />
                        <input
                            type="text"
                            name="title"
                            placeholder="Qual a atividade"
                            className="bg-transparent text-lg placeholder-zinc-400 flex-1 outline-none"
                        />
                    </div>
                    <div className="flex items-center gap-2">
                        <div className="h-14 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex items-center gap-2 flex-1">
                            <Calendar className=" text-zinc-400 size-5" />
                            <input
                                type="date"
                                name="date"
                                className="bg-transparent text-lg placeholder-zinc-400 flex-1 outline-none"
                            />
                        </div>
                        <div className="h-14 w-40 px-4 bg-zinc-950 border border-zinc-800 rounded-lg flex items-center gap-2">
                            <Clock className=" text-zinc-400 size-5" />
                            <input
                                type="time"
                                name="time"
                                className="bg-transparent text-lg placeholder-zinc-400 flex-1 outline-none"
                            />
                        </div>
                    </div>
                    <Button type="submit" variant="primary" size="full">
                        Salvar atividade
                        <CircleCheckBig className="size-5" />
                    </Button>
                </form>
            </div>
        </div>
    )
}