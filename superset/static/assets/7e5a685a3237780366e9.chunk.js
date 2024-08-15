"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[49173],{727989:(e,t,a)=>{a.d(t,{Z:()=>v});var o=a(150361),l=a.n(o),s=a(667294),n=a(748086),r=a(970553),i=a(751995),d=a(431069),u=a(455867),c=a(268084),p=a(835932),h=a(774069),m=a(49937),g=a(34858),y=a(762921),b=a(211965);const Z=i.iK.div`
  display: block;
  color: ${({theme:e})=>e.colors.grayscale.base};
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
`,w=i.iK.div`
  padding-bottom: ${({theme:e})=>2*e.gridUnit}px;
  padding-top: ${({theme:e})=>2*e.gridUnit}px;

  & > div {
    margin: ${({theme:e})=>e.gridUnit}px 0;
  }

  &.extra-container {
    padding-top: 8px;
  }

  .confirm-overwrite {
    margin-bottom: ${({theme:e})=>2*e.gridUnit}px;
  }

  .input-container {
    display: flex;
    align-items: center;

    label {
      display: flex;
      margin-right: ${({theme:e})=>2*e.gridUnit}px;
    }

    i {
      margin: 0 ${({theme:e})=>e.gridUnit}px;
    }
  }

  input,
  textarea {
    flex: 1 1 auto;
  }

  textarea {
    height: 160px;
    resize: none;
  }

  input::placeholder,
  textarea::placeholder {
    color: ${({theme:e})=>e.colors.grayscale.light1};
  }

  textarea,
  input[type='text'],
  input[type='number'] {
    padding: ${({theme:e})=>1.5*e.gridUnit}px
      ${({theme:e})=>2*e.gridUnit}px;
    border-style: none;
    border: 1px solid ${({theme:e})=>e.colors.grayscale.light2};
    border-radius: ${({theme:e})=>e.gridUnit}px;

    &[name='name'] {
      flex: 0 1 auto;
      width: 40%;
    }

    &[name='sqlalchemy_uri'] {
      margin-right: ${({theme:e})=>3*e.gridUnit}px;
    }
  }
`,v=({resourceName:e,resourceLabel:t,passwordsNeededMessage:a,confirmOverwriteMessage:o,onModelImport:i,show:v,onHide:f,passwordFields:x=[],setPasswordFields:S=(()=>{}),DealList:k})=>{const[C,$]=(0,s.useState)(!0),[q,D]=(0,s.useState)(!1),[_,T]=(0,s.useState)({}),[I,P]=(0,s.useState)(!1),[E,N]=(0,s.useState)(!1),[H,z]=(0,s.useState)([]),[F,U]=(0,s.useState)(!1),[B,M]=(0,s.useState)(),[O,R]=(0,s.useState)([]),[j,L]=(0,s.useState)(null),[A,Q]=(0,s.useState)([]),[K,V]=(0,s.useState)(null),[Y,W]=(0,s.useState)([]),[X,G]=(0,s.useState)(null),[J,ee]=(0,s.useState)([]),[te,ae]=(0,s.useState)(null),oe=()=>{z([]),S([]),T({}),P(!1),N(!1),U(!1),M(""),L(null),V(null),G(null),ae(null)};(0,s.useEffect)((()=>{v&&!q&&(le("datasource"),"dataset"==e&&le("dataset"),"chart"==e&&(le("dataset"),le("chart")),"dashboard"==e&&(le("dataset"),le("chart"),le("dashboard")))}),[v]);const le=e=>{d.Z.get({endpoint:`/api/v2/${e}/group/`}).then((t=>{if(200==t.json.meta.code||201==t.json.meta.code){const a=se(l()(t.json.meta.data),"");"dataset"==e&&R(a),"datasource"==e&&Q(a),"chart"==e&&W(a),"dashboard"==e&&ee(a),D(!0)}else D(!1),n.ZP.error(t.json.meta.message)}))},se=(e,t)=>{const a=[];return e.forEach((e=>{const o={title:e.name,allname:`${t?t+"-":""}${e.name}`,key:e.group_id,value:e.group_id,disabled:e.perm<4,children:se(e.children,e.name)};(!o.disabled||o.children.length>0)&&a.push(o)})),a},{state:{alreadyExists:ne,passwordsNeeded:re},importResource:ie}=(0,g.PW)(e,t,(e=>{M(e)}));(0,s.useEffect)((()=>{S(re),re.length>0&&U(!1)}),[re,S]),(0,s.useEffect)((()=>{P(ne.length>0),ne.length>0&&U(!1)}),[ne,P]);const de=e=>{var t,a;const o=null!=(t=null==(a=e.currentTarget)?void 0:a.value)?t:"";N(o.toUpperCase()===(0,u.t)("OVERWRITE"))};C&&v&&$(!1);return(0,b.tZ)(h.Z,{name:"model",className:"import-model-modal",disablePrimaryButton:0===H.length||I&&!E||F,onHandledPrimaryAction:()=>{var t;if(!((null==(t=H[0])?void 0:t.originFileObj)instanceof File))return;let a=j,o=K,l=X,s=te;return o&&("dataset"!=e||a)&&("chart"!=e||l||a)&&("dashboard"!=e||l||s||a)?(U(!0),ie(H[0].originFileObj,_,E,a,o,l,s).then((e=>!!e&&(n.ZP.success((0,u.t)("success")),oe(),i(),null==k||k(),!1))),!1):n.ZP.error((0,u.t)("Select Group"))},onHide:()=>{$(!0),f(),oe()},primaryButtonName:I?(0,u.t)("Overwrite"):(0,u.t)("Import"),primaryButtonType:I?"danger":"primary",width:"750px",show:v,title:(0,b.tZ)("h4",null,(0,u.t)("Import %s",t))},(0,b.tZ)(w,null,(0,b.tZ)("div",null,("chart"==e||"dashboard"==e||"dataset"==e)&&(0,b.tZ)("div",{style:{marginBottom:"20px"}},(0,b.tZ)("span",null,(0,b.tZ)("span",{style:{color:"red"}},"*"),(0,u.t)("dataset"),"\uff1a"),(0,b.tZ)(r.Z,{showSearch:!0,style:{width:"300px"},value:j,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,u.t)("Please select"),allowClear:!0,treeDefaultExpandAll:!0,onChange:e=>{L(e)},treeData:O,treeNodeFilterProp:"title",treeIcon:!0,suffixIcon:(0,b.tZ)(c.default,null)})),(0,b.tZ)("div",{style:{marginBottom:"20px"}},(0,b.tZ)("span",null,(0,b.tZ)("span",{style:{color:"red"}},"*"),(0,u.t)("database"),"\uff1a"),(0,b.tZ)(r.Z,{showSearch:!0,style:{width:"300px"},value:K,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,u.t)("Please select"),allowClear:!0,treeDefaultExpandAll:!0,onChange:e=>{V(e)},treeData:A,treeNodeFilterProp:"title",treeIcon:!0,suffixIcon:(0,b.tZ)(c.default,null)})),("chart"==e||"dashboard"==e)&&(0,b.tZ)("div",{style:{marginBottom:"20px"}},(0,b.tZ)("span",{style:{display:"inline-block",width:"62px"}},(0,b.tZ)("span",{style:{color:"red"}},"*"),(0,u.t)("chart"),"\uff1a"),(0,b.tZ)(r.Z,{showSearch:!0,style:{width:"300px"},value:X,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,u.t)("Please select"),allowClear:!0,treeDefaultExpandAll:!0,onChange:e=>{G(e)},treeData:Y,treeNodeFilterProp:"title",treeIcon:!0,suffixIcon:(0,b.tZ)(c.default,null)})),"dashboard"==e&&(0,b.tZ)("div",{style:{marginBottom:"20px"}},(0,b.tZ)("span",{style:{display:"inline-block",width:"62px"}},(0,b.tZ)("span",{style:{color:"red"}},"*"),(0,u.t)("dashboard"),"\uff1a"),(0,b.tZ)(r.Z,{showSearch:!0,style:{width:"300px"},value:te,dropdownStyle:{maxHeight:400,overflow:"auto"},placeholder:(0,u.t)("Please select"),allowClear:!0,treeDefaultExpandAll:!0,onChange:e=>{ae(e)},treeData:J,treeNodeFilterProp:"title",treeIcon:!0,suffixIcon:(0,b.tZ)(c.default,null)})),(0,b.tZ)(m.gq,{name:"modelFile",id:"modelFile","data-test":"model-file-input",accept:".yaml,.json,.yml,.zip",fileList:H,onChange:e=>{z([{...e.file,status:"done"}])},onRemove:e=>(z(H.filter((t=>t.uid!==e.uid))),!1),customRequest:()=>{},disabled:F},(0,b.tZ)(p.Z,{loading:F},(0,u.t)("Select file"))))),B&&(0,b.tZ)(y.Z,{errorMessage:B,showDbInstallInstructions:x.length>0}),0===x.length?null:(0,b.tZ)(s.Fragment,null,(0,b.tZ)("h5",null,(0,u.t)("Database passwords")),(0,b.tZ)(Z,null,a),x.map((e=>(0,b.tZ)(w,{key:`password-for-${e}`},(0,b.tZ)("div",{className:"control-label"},e,(0,b.tZ)("span",{className:"required"},"*")),(0,b.tZ)("input",{name:`password-${e}`,autoComplete:`password-${e}`,type:"password",value:_[e],onChange:t=>T({..._,[e]:t.target.value})}))))),I?(0,b.tZ)(s.Fragment,null,(0,b.tZ)(w,null,(0,b.tZ)("div",{className:"confirm-overwrite"},o),(0,b.tZ)("div",{className:"control-label"},(0,u.t)('Type "%s" to confirm',(0,u.t)("OVERWRITE"))),(0,b.tZ)("input",{"data-test":"overwrite-modal-input",id:"overwrite",type:"text",onChange:de}))):null)}},129848:(e,t,a)=>{a.d(t,{Z:()=>d});a(667294);var o=a(751995),l=a(358593),s=a(731293),n=a(211965);const r=o.iK.span`
  white-space: nowrap;
  min-width: 100px;
  svg,
  i {
    margin-right: 8px;

    &:hover {
      path {
        fill: ${({theme:e})=>e.colors.primary.base};
      }
    }
  }
`,i=o.iK.span`
  color: ${({theme:e})=>e.colors.grayscale.base};
`;function d({actions:e}){return(0,n.tZ)(r,{className:"actions"},e.map(((e,t)=>{const a=s.Z[e.icon];return e.tooltip?(0,n.tZ)(l.u,{id:`${e.label}-tooltip`,title:e.tooltip,placement:e.placement,key:t},(0,n.tZ)(i,{role:"button",tabIndex:0,className:"action-button","data-test":e.label,onClick:e.onClick},(0,n.tZ)(a,null))):(0,n.tZ)(i,{role:"button",tabIndex:0,className:"action-button",onClick:e.onClick,"data-test":e.label,key:t},(0,n.tZ)(a,null))})))}},549588:(e,t,a)=>{a.r(t),a.d(t,{default:()=>j});var o=a(455867),l=a(751995),s=a(431069),n=a(667294),r=a(115926),i=a.n(r),d=a(730381),u=a.n(d),c=a(667496),p=a(440768),h=a(976697),m=a(414114),g=a(34858),y=a(419259),b=a(232228),Z=a(620755),w=a(418782),v=a(838703),f=a(217198),x=a(129848),S=a(358593),k=a(495413),C=a(710222),$=a(591877),q=a(593185),D=a(727989),_=a(731293),T=a(774069),I=a(835932),P=a(331673),E=a(14025),N=a(211965);const H=l.iK.div`
  color: ${({theme:e})=>e.colors.secondary.light2};
  font-size: ${({theme:e})=>e.typography.sizes.s}px;
  margin-bottom: 0;
  text-transform: uppercase;
`,z=l.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark2};
  font-size: ${({theme:e})=>e.typography.sizes.m}px;
  padding: 4px 0 16px 0;
`,F=(0,l.iK)(T.Z)`
  .ant-modal-content {
  }

  .ant-modal-body {
    padding: 24px;
  }

  pre {
    font-size: ${({theme:e})=>e.typography.sizes.xs}px;
    font-weight: ${({theme:e})=>e.typography.weights.normal};
    line-height: ${({theme:e})=>e.typography.sizes.l}px;
    height: 375px;
    border: none;
  }
`,U=(0,m.ZP)((({fetchData:e,onHide:t,openInSqlLab:a,queries:l,savedQuery:s,show:r,addDangerToast:i,addSuccessToast:d})=>{const{handleKeyPress:u,handleDataChange:c,disablePrevious:p,disableNext:h}=(0,E.Cq)({queries:l,currentQueryId:s.id,fetchData:e});return(0,N.tZ)("div",{role:"none",onKeyUp:u},(0,N.tZ)(F,{onHide:t,show:r,title:(0,o.t)("Query preview"),footer:(0,N.tZ)(n.Fragment,null,(0,N.tZ)(I.Z,{"data-test":"previous-saved-query",key:"previous-saved-query",disabled:p,onClick:()=>c(!0)},(0,o.t)("Previous")),(0,N.tZ)(I.Z,{"data-test":"next-saved-query",key:"next-saved-query",disabled:h,onClick:()=>c(!1)},(0,o.t)("Next")),(0,N.tZ)(I.Z,{"data-test":"open-in-sql-lab",key:"open-in-sql-lab",buttonStyle:"primary",onClick:()=>a(s.id)},(0,o.t)("Open in SQL Lab")))},(0,N.tZ)(H,null,(0,o.t)("Query name")),(0,N.tZ)(z,null,s.label),(0,N.tZ)(P.Z,{language:"sql",addDangerToast:i,addSuccessToast:d},s.sql||"")))})),B=(0,o.t)('The passwords for the databases below are needed in order to import them together with the saved queries. Please note that the "Secure Extra" and "Certificate" sections of the database configuration are not present in export files, and should be added manually after the import if they are needed.'),M=(0,o.t)("You are importing one or more saved queries that already exist. Overwriting might cause you to lose some of your work. Are you sure you want to overwrite?"),O=l.iK.div`
  .count {
    margin-left: 5px;
    color: ${({theme:e})=>e.colors.primary.base};
    text-decoration: underline;
    cursor: pointer;
  }
`,R=l.iK.div`
  color: ${({theme:e})=>e.colors.grayscale.dark2};
`;const j=(0,m.ZP)((function({addDangerToast:e,addSuccessToast:t}){const{state:{loading:a,resourceCount:l,resourceCollection:r,bulkSelectEnabled:d},hasPerm:m,fetchData:T,toggleBulkSelect:I,refreshData:P}=(0,g.Yi)("saved_query",(0,o.t)("Saved queries"),e),[E,H]=(0,n.useState)(null),[z,F]=(0,n.useState)(null),[j,L]=(0,n.useState)(!1),[A,Q]=(0,n.useState)([]),[K,V]=(0,n.useState)(!1),[Y,W]=(0,n.useState)(void 0),X=()=>{L(!0)},G=m("can_write"),J=m("can_write"),ee=m("can_write"),te=m("can_export")&&(0,$.cr)(q.T.VERSIONED_EXPORT),ae=(0,n.useCallback)((t=>{s.Z.get({endpoint:`/api/v1/saved_query/${t}`}).then((({json:e={}})=>{F({...e.result})}),(0,p.v$)((t=>e((0,o.t)("There was an issue previewing the selected query %s",t)))))}),[e]),oe=[];k.Y.tabs.map((e=>{e.show&&oe.push(e)}));const le={activeChild:"Saved queries",...k.Y,tabs:oe},se=[];ee&&se.push({name:(0,o.t)("Bulk select"),onClick:I,buttonStyle:"secondary"}),se.push({name:(0,N.tZ)(n.Fragment,null,(0,N.tZ)("i",{className:"fa fa-plus"})," ",(0,o.t)("Query")),onClick:()=>{window.open(`${window.location.origin}${(0,c.VU)("/superset/sqllab?new=true")}`)},buttonStyle:"primary"}),G&&(0,$.cr)(q.T.VERSIONED_EXPORT)&&se.push({name:(0,N.tZ)(S.u,{id:"import-tooltip",title:(0,o.t)("Import queries"),placement:"bottomRight","data-test":"import-tooltip-test"},(0,N.tZ)(_.Z.Import,{"data-test":"import-icon"})),buttonStyle:"link",onClick:X,"data-test":"import-button"}),le.buttons=se;const ne=e=>{window.open(`${window.location.origin}${(0,c.VU)(`/superset/sqllab?savedQueryId=${e}`)}`)},re=(0,n.useCallback)((a=>{(0,C.Z)((()=>Promise.resolve(`${window.location.origin}${(0,c.VU)(`/superset/sqllab?savedQueryId=${a}`)}`))).then((()=>{t((0,o.t)("Link Copied!"))})).catch((()=>{e((0,o.t)("Sorry, your browser does not support copying."))}))}),[e,t]),ie=e=>{const t=e.map((({id:e})=>e));(0,b.Z)("saved_query",t,(()=>{V(!1)})),V(!0)},de=[{id:"changed_on_delta_humanized",desc:!0}],ue=(0,n.useMemo)((()=>[{accessor:"label",Header:(0,o.t)("Name")},{accessor:"database.database_name",Header:(0,o.t)("Database"),size:"xl"},{accessor:"database",hidden:!0,disableSortBy:!0},{accessor:"schema",Header:(0,o.t)("Schema"),size:"xl"},{Cell:({row:{original:{sql_tables:e=[]}}})=>{const t=e.map((e=>e.table)),a=(null==t?void 0:t.shift())||"";return t.length?(0,N.tZ)(O,null,(0,N.tZ)("span",null,a),(0,N.tZ)(h.ZP,{placement:"right",title:(0,o.t)("TABLES"),trigger:"click",content:(0,N.tZ)(n.Fragment,null,t.map((e=>(0,N.tZ)(R,{key:e},e))))},(0,N.tZ)("span",{className:"count"},"(+",t.length,")"))):a},accessor:"sql_tables",Header:(0,o.t)("Tables"),size:"xl",disableSortBy:!0},{Cell:({row:{original:{created_on:e}}})=>{const t=new Date(e),a=new Date(Date.UTC(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes(),t.getSeconds(),t.getMilliseconds()));return u()(a).fromNow()},Header:(0,o.t)("Created on"),accessor:"created_on",size:"xl"},{Cell:({row:{original:{changed_on_delta_humanized:e}}})=>e,Header:(0,o.t)("Modified"),accessor:"changed_on_delta_humanized",size:"xl"},{Cell:({row:{original:e}})=>{const t=[{label:"preview-action",tooltip:(0,o.t)("Query preview"),placement:"bottom",icon:"Binoculars",onClick:()=>{ae(e.id)}},J&&{label:"edit-action",tooltip:(0,o.t)("Edit query"),placement:"bottom",icon:"Edit",onClick:()=>ne(e.id)},{label:"copy-action",tooltip:(0,o.t)("Copy query URL"),placement:"bottom",icon:"Copy",onClick:()=>re(e.id)},te&&{label:"export-action",tooltip:(0,o.t)("Export query"),placement:"bottom",icon:"Share",onClick:()=>ie([e])},ee&&{label:"delete-action",tooltip:(0,o.t)("Delete query"),placement:"bottom",icon:"Trash",onClick:()=>H(e)}].filter((e=>!!e));return(0,N.tZ)(x.Z,{actions:t})},Header:(0,o.t)("Actions"),id:"actions",disableSortBy:!0}]),[ee,J,te,re,ae]),ce=(0,n.useMemo)((()=>async()=>s.Z.get({endpoint:"/api/v2/datasource/database/list/"}).then((e=>{var t,a,o;return e.json.meta.data=(null==e||null==(t=e.json)||null==(a=t.meta)||null==(o=a.data)?void 0:o.map((e=>({value:e.id,label:e.database_name}))))||[],e.json.meta}))),[]),pe=(0,n.useCallback)((()=>{const e=`/api/v1/database/${Y}/schemas/`;return s.Z.get({endpoint:e}).then((e=>({data:e.json.result.map((e=>({value:e,label:e})))||[]})))}),[Y]),he=(0,n.useMemo)((()=>[{Header:(0,o.t)("Database"),key:"database",id:"database",input:"select",operator:w.p.relationOneMany,unfilteredLabel:(0,o.t)("All"),fetchSelects:ce,onFilterUpdate:e=>W(null==e?void 0:e.value),paginate:!0},{Header:(0,o.t)("Schema"),id:"schema",key:"schema",input:"select",operator:w.p.equals,unfilteredLabel:"All",fetchSelects:pe,paginate:!0},{Header:(0,o.t)("Search"),id:"label",key:"search",input:"search",operator:w.p.allText}]),[e,pe]);return(0,N.tZ)("div",{style:{paddingTop:50}},(0,N.tZ)(Z.Z,le),E&&(0,N.tZ)(f.Z,{description:(0,o.t)("This action will permanently delete the saved query."),onConfirm:()=>{E&&(({id:a,label:l})=>{s.Z.delete({endpoint:`/api/v1/saved_query/${a}`}).then((()=>{P(),H(null),t((0,o.t)("Deleted: %s",l))}),(0,p.v$)((t=>e((0,o.t)("There was an issue deleting %s: %s",l,t)))))})(E)},onHide:()=>H(null),open:!0,title:(0,o.t)("Delete Query?")}),z&&(0,N.tZ)(U,{fetchData:ae,onHide:()=>F(null),savedQuery:z,queries:r,openInSqlLab:ne,show:!0}),(0,N.tZ)(y.Z,{title:(0,o.t)("Please confirm"),description:(0,o.t)("Are you sure you want to delete the selected queries?"),onConfirm:a=>{s.Z.delete({endpoint:`/api/v1/saved_query/?q=${i().encode(a.map((({id:e})=>e)))}`}).then((({json:e={}})=>{P(),t(e.message)}),(0,p.v$)((t=>e((0,o.t)("There was an issue deleting the selected queries: %s",t)))))}},(e=>{const t=[];return ee&&t.push({key:"delete",name:(0,o.t)("Delete"),onSelect:e,type:"danger"}),te&&t.push({key:"export",name:(0,o.t)("Export"),type:"primary",onSelect:ie}),(0,N.tZ)(w.Z,{className:"saved_query-list-view",columns:ue,count:l,data:r,fetchData:T,filters:he,initialSort:de,loading:a,pageSize:25,bulkActions:t,bulkSelectEnabled:d,disableBulkSelect:I,highlightRowId:null==z?void 0:z.id})})),(0,N.tZ)(D.Z,{resourceName:"saved_query",resourceLabel:(0,o.t)("queries"),passwordsNeededMessage:B,confirmOverwriteMessage:M,addDangerToast:e,addSuccessToast:t,onModelImport:()=>{L(!1),P(),t((0,o.t)("Query imported"))},show:j,onHide:()=>{L(!1)},passwordFields:A,setPasswordFields:Q}),K&&(0,N.tZ)(v.Z,null))}))}}]);