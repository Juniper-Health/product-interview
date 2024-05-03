import { FunctionComponent } from 'react';
import Sidebar from '../SideBar/SideBar';
import { Helmet } from 'react-helmet-async';
import logoSrc from '../../assets/img/logo.png';
import MenuIcon from '@mui/icons-material/Menu';
import styles from './styles.module.scss';

interface Props {
    title: string;
    children: React.ReactNode;
}

const PageContainer: FunctionComponent<Props> = ({ title, children }) => {
    return (
        <>
            <Helmet>
                <title>{title}</title>
            </Helmet>
            <main className={styles['container']}>
                <div className={styles['topBar']}>
                    <div className={styles['topBarLeft']}>
                        <button className={styles['sidebarToggleButton']}>
                            <MenuIcon />
                        </button>
                        <img
                            className={styles['logo']}
                            src={logoSrc}
                            alt="Logo"
                        />
                        <div className={styles['clinicName']}>
                            Juniper Programming Interview
                        </div>
                    </div>
                </div>
                <div className={styles['sideBarAndContent']}>
                    <Sidebar />
                    <div className={styles['contentContainer']}>
                        <div className={styles['content']}>{children}</div>
                    </div>
                </div>
            </main>
        </>
    );
};

export default PageContainer;
