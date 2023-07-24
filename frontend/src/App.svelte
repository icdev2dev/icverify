<script>
  import { Route, Router, Link } from "svelte-routing";
  let basepath = "/";
  let path = location.pathname;

  import Header from "./lib/Header.svelte";

  import HomePage from "./lib/pages/HomePage.svelte";
  import HomeTab from "./lib/tabs/HomeTab.svelte";

  import ProposalsPage from "./lib/pages/ProposalsPage.svelte";
  import ProposalsTab from "./lib/tabs/ProposalsTab.svelte";

  import ReplicaVerificationPage from "./lib/pages/ReplicaVerificationPage.svelte";
  import ReplicaVerificationTab from "./lib/tabs/ReplicaVerificationTab.svelte";

  import SettingsPage from "./lib/pages/SettingsPage.svelte";
  import SettingsTab from "./lib/tabs/SettingsTab.svelte";

  import NotificationsPage from "./lib/pages/NotificationsPage.svelte";
  import NotificationsTab from "./lib/tabs/NotificationsTab.svelte";

</script>

<Header>

</Header>

<hr class="solid">

<Router {basepath}>

  <div id="maintabs" on:click={() => (path = location.pathname)}>
    <nav>
      <ul>
         <li> 
          <Link to="/">
            <HomeTab/>
          </Link>
        </li>
        <li>
          <Link to="/proposals">
            <ProposalsTab>

            </ProposalsTab>
            
          </Link>
        </li>
        <li>
          <Link to="/replicaverification">
            <ReplicaVerificationTab>
            </ReplicaVerificationTab>
          </Link>
        </li>
        <li>
          <Link to="/notifications">
            <NotificationsTab>

            </NotificationsTab>
            
          </Link>
        </li>

        <li>
          <Link to="/settings">
            <SettingsTab>

            </SettingsTab>
            
          </Link>
        </li>
    </ul>
  </nav>
  </div>
  


  <main>
    You are here: <code>{path}</code>

    <Route path="/">
      <HomePage>
      </HomePage>
    </Route>

    <Route path="/proposals">
      <ProposalsPage>

      </ProposalsPage>
      
    </Route>

    <Route path="/replicaverification">
      <ReplicaVerificationPage>

      </ReplicaVerificationPage> 
    </Route>

    <Route path="/notifications">
      <NotificationsPage>

      </NotificationsPage>
    </Route>

    <Route path="/settings">
      <SettingsPage>

      </SettingsPage>
      
    </Route>
  </main>
</Router>








<style>


nav {
    background-color: #f8f9fa;
    padding: 10px;
  }

  ul {
    display: flex;
    justify-content: space-around;
    list-style-type: none;
    
  }

  li {
    cursor: pointer;
    margin-left: 100px;
    margin-right: 100px;
    
  }

  hr.solid {
    border-top: 3px solid #bbb;
  }


  
</style>