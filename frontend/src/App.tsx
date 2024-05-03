import { FunctionComponent } from 'react';
import {
    Router,
    Switch,
    Route,
} from 'react-router-dom';
import { HelmetProvider } from 'react-helmet-async';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import { createBrowserHistory } from 'history';
import SamplePage from './components/SamplePage/SamplePage';

const queryClient = new QueryClient({
    defaultOptions: {
        queries: {
            retry: false,
            staleTime: Infinity,
            refetchOnWindowFocus: false,
            refetchOnReconnect: false,
        },
    },
});


const App: FunctionComponent = () => (
  <HelmetProvider>
    <QueryClientProvider client={queryClient}>
      <ReactQueryDevtools initialIsOpen={false} />
      <Router history={createBrowserHistory()}>
          <Switch>
          <Route path='*'>
              <SamplePage />
          </Route>
          </Switch>
      </Router>
    </QueryClientProvider>
  </HelmetProvider>
);

export default App;
