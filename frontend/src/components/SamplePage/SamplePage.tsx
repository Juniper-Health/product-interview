import { FunctionComponent } from "react";
import PageContainer from "../PageContainer/PageContainer";
import { Typography } from "@mui/material";
import { useQuery } from "@tanstack/react-query";
import { getPatients } from "../../queries/queries";

const SamplePage: FunctionComponent = () => {
    const { isLoading, isError, data, error } = useQuery({
        queryKey: ['patients'],
        queryFn: getPatients,
    })

    return (
        <PageContainer title="Sample Page">
            <Typography>Check Out SamplePage.tsx</Typography>
        </PageContainer>
    )
}

export default SamplePage;