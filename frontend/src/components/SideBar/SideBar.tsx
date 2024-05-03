import { Link } from 'react-router-dom';
import {
    DashboardOutlined,
} from '@mui/icons-material';
import { FunctionComponent } from 'react';
import styles from './styles.module.scss';

const SideBar: FunctionComponent = () => {
    return (
        <div
            className={`${styles['container']}`}
        >
            <nav role="navigation" aria-label="Page Navigation">
                <ul className={styles['linkContainer']}>
                    <li
                        className={`${styles['linkItem']} ${styles['linkItemBackground']}`}
                    >
                        <Link
                            to={'/'}
                            className={styles['link']}
                        >
                            <DashboardOutlined style={{ color: '#859CA9' }} />{' '}
                            Solution
                        </Link>
                    </li>
                </ul>
            </nav>
        </div>
    );
};

export default SideBar;
