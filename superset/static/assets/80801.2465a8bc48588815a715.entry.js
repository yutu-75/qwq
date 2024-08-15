"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[80801],{166683:(e,t,i)=>{i.d(t,{Z:()=>h});var r=i(667294),l=i(855241),a=i(751995),n=i(455867),s=i(877998),o=i(211965);const d=a.iK.span`
  ${({theme:e})=>"\n    margin-left: 10px;\n    font-size: 14px;\n"}
`,c=a.iK.div`
  ${({theme:e})=>`\n        p {\n            font-size: ${e.typography.sizes.s}\n            color: ${e.colors.grayscale.dark2};\n            font-weight: ${e.typography.weights.bold};\n            span {\n                color: ${e.colors.grayscale.dark1};\n                font-weight: ${e.typography.weights.medium};\n            }\n        }\n    `}
`;function h(e){const t=(0,r.useCallback)((()=>{const{created_on:t,created_by:i,changed_on:r,changed_by:l}=e;return(0,o.tZ)(c,null,(0,o.tZ)("p",null,(0,n.t)("Has created by"),"\uff1a",(0,o.tZ)("span",null,i)),(0,o.tZ)("p",null,(0,n.t)("created time"),"\uff1a",(0,o.tZ)("span",null,t)),(0,o.tZ)("p",null,(0,n.t)("Last modified"),"\uff1a",(0,o.tZ)("span",null,l)),(0,o.tZ)("p",null,(0,n.t)("Modify time"),"\uff1a",(0,o.tZ)("span",null,r)))}),[e]);return(0,o.tZ)(l.Z,{content:t},(0,o.tZ)(d,null,(0,o.tZ)(s.default,null)))}},602275:(e,t,i)=>{i.d(t,{$6:()=>d,$X:()=>u,DZ:()=>p,Er:()=>h,Rw:()=>c,cP:()=>o,ck:()=>b});var r=i(45697),l=i.n(r),a=i(81255),n=i(400713),s=i(879271);const o=l().shape({id:l().string.isRequired,type:l().oneOf(Object.values(a.ZP)).isRequired,parents:l().arrayOf(l().string),children:l().arrayOf(l().string),meta:l().shape({width:l().number,height:l().number,headerSize:l().oneOf(s.Z.map((e=>e.value))),background:l().oneOf(n.Z.map((e=>e.value))),chartId:l().number})}),d=l().shape({id:l().number.isRequired,chartAlert:l().string,chartStatus:l().string,chartUpdateEndTime:l().number,chartUpdateStartTime:l().number,latestQueryFormData:l().object,queryController:l().shape({abort:l().func}),queriesResponse:l().arrayOf(l().object),triggerQuery:l().bool,lastRendered:l().number}),c=l().shape({slice_id:l().number.isRequired,slice_url:l().string.isRequired,slice_name:l().string.isRequired,datasource:l().string,datasource_name:l().string,datasource_link:l().string,changed_on:l().number.isRequired,modified:l().string,viz_type:l().string.isRequired,description:l().string,description_markeddown:l().string,owners:l().arrayOf(l().string)}),h=l().shape({chartId:l().number.isRequired,componentId:l().string.isRequired,filterName:l().string.isRequired,datasourceId:l().string.isRequired,directPathToFilter:l().arrayOf(l().string).isRequired,isDateFilter:l().bool.isRequired,isInstantFilter:l().bool.isRequired,columns:l().object,labels:l().object,scopes:l().object}),p=l().shape({sliceIds:l().arrayOf(l().number),expandedSlices:l().object,editMode:l().bool,isPublished:l().bool,colorNamespace:l().string,colorScheme:l().string,updatedColorScheme:l().bool,hasUnsavedChanges:l().bool}),u=l().shape({id:l().number,metadata:l().object,slug:l().string,dash_edit_perm:l().bool,dash_save_perm:l().bool,common:l().object,userId:l().string}),m=l().shape({value:l().oneOfType([l().number,l().string]).isRequired,label:l().string.isRequired}),g={value:l().oneOfType([l().number,l().string]).isRequired,label:l().string.isRequired,children:l().arrayOf(l().oneOfType([l().shape((f=()=>g,()=>f().apply(void 0,arguments))),m]))};var f;const b=l().oneOfType([l().shape(g),m])},679789:(e,t,i)=>{i.d(t,{Z:()=>d});var r=i(667294),l=i(751995),a=i(455867),n=i(731293),s=i(358593),o=i(211965);const d=function({certifiedBy:e,details:t,size:i="l"}){const d=(0,l.Fg)();return(0,o.tZ)(s.u,{id:"certified-details-tooltip",title:(0,o.tZ)(r.Fragment,null,e&&(0,o.tZ)("div",null,(0,o.tZ)("strong",null,(0,a.t)("Certified by %s",e))),(0,o.tZ)("div",null,t))},(0,o.tZ)(n.Z.Certified,{iconColor:d.colors.primary.base,iconSize:i}))}},217198:(e,t,i)=>{i.d(t,{Z:()=>p});var r=i(751995),l=i(455867),a=i(667294),n=i(9875),s=i(774069),o=i(49238),d=i(211965);const c=r.iK.div`
  padding-top: 8px;
  width: 50%;
  label {
    color: ${({theme:e})=>e.colors.grayscale.base};
    text-transform: uppercase;
  }
`,h=r.iK.div`
  line-height: 40px;
  padding-top: 16px;
`;function p({description:e,onConfirm:t,onHide:i,open:r,title:p}){const[u,m]=(0,a.useState)(!0),[g,f]=(0,a.useState)(""),b=()=>{f(""),t()};return(0,d.tZ)(s.Z,{disablePrimaryButton:u,onHide:()=>{f(""),i()},onHandledPrimaryAction:b,primaryButtonName:(0,l.t)("Delete"),primaryButtonType:"danger",show:r,title:p},(0,d.tZ)(h,null,e),(0,d.tZ)(c,null,(0,d.tZ)(o.lX,{htmlFor:"delete"},(0,l.t)('Type "%s" to confirm',(0,l.t)("DELETE"))),(0,d.tZ)(n.II,{"data-test":"delete-modal-input",type:"text",id:"delete",autoComplete:"off",value:g,onChange:e=>{var t;const i=null!=(t=e.target.value)?t:"";m(i.toUpperCase()!==(0,l.t)("DELETE")),f(i)},onPressEnter:()=>{u||b()}})))}},236674:(e,t,i)=>{i.d(t,{Z:()=>h});var r=i(667294),l=i(751995),a=i(211965),n=i(455867),s=i(358593),o=i(833626),d=i(731293);const c=l.iK.a`
  ${({theme:e})=>a.iv`
    font-size: ${e.typography.sizes.xl}px;
    display: flex;
    padding: 0 0 0 ${2*e.gridUnit}px;
  `};
`,h=({itemId:e,isStarred:t,showTooltip:i,saveFaveStar:l,fetchFaveStar:h})=>{(0,o.J)((()=>{h&&h(e)}));const p=(0,r.useCallback)((i=>{i.preventDefault(),l(e,!!t)}),[t,e,l]),u=(0,a.tZ)(c,{href:"#",onClick:p,className:"fave-unfave-icon","data-test":"fave-unfave-icon",role:"button"},t?(0,a.tZ)(d.Z.FavoriteSelected,null):(0,a.tZ)(d.Z.FavoriteUnselected,null));return i?(0,a.tZ)(s.u,{id:"fave-unfave-tooltip",title:(0,n.t)("Click to favorite/unfavorite")},u):u}},720818:(e,t,i)=>{i.d(t,{Z:()=>M});var r=i(667294),l=i(9875),a=i(49238),n=i(151127),s=i.n(n),o=i(835932),d=i(49937),c=i(115926),h=i.n(c),p=i(751995),u=i(455867),m=i(281545),g=i(431069),f=i(355786),b=i(478161),y=i(328062),v=i(774069),F=i(794670),x=i(45697),Z=i.n(x),C=i(676787),k=i(211965);const S={onChange:Z().func,labelMargin:Z().number,colorScheme:Z().string,hasCustomLabelColors:Z().bool},$={hasCustomLabelColors:!1,colorScheme:void 0,onChange:()=>{}};class w extends r.PureComponent{constructor(e){super(e),this.state={hovered:!1},this.categoricalSchemeRegistry=(0,m.Z)(),this.choices=this.categoricalSchemeRegistry.keys().map((e=>[e,e])),this.schemes=this.categoricalSchemeRegistry.getMap()}setHover(e){this.setState({hovered:e})}render(){const{colorScheme:e,labelMargin:t=0,hasCustomLabelColors:i}=this.props;return(0,k.tZ)(C.Z,{description:(0,u.t)("Any color palette selected here will override the colors applied to this dashboard's individual charts"),labelMargin:t,name:"color_scheme",onChange:this.props.onChange,value:e,choices:this.choices,clearable:!0,schemes:this.schemes,hovered:this.state.hovered,hasCustomLabelColors:i})}}w.propTypes=S,w.defaultProps=$;const N=w;var _=i(968084),I=i(998286),O=i(414114),U=i(591877),E=i(593185);const R=(0,p.iK)(a.xJ)`
  margin-bottom: 0;
`,T=(0,p.iK)(F.Ad)`
  border-radius: ${({theme:e})=>e.borderRadius}px;
  border: 1px solid ${({theme:e})=>e.colors.secondary.light2};
`,M=(0,O.ZP)((({addSuccessToast:e,addDangerToast:t,colorScheme:i,dashboardId:n,dashboardInfo:c,dashboardTitle:p,onHide:x=(()=>{}),onlyApply:Z=!1,onSubmit:C=(()=>{}),show:S=!1})=>{const[$]=d.qz.useForm(),[w,O]=(0,r.useState)(!1),[M,q]=(0,r.useState)(!1),[j,A]=(0,r.useState)(i),[z,K]=(0,r.useState)(""),[L,X]=(0,r.useState)(),[D,J]=(0,r.useState)([]),[B,P]=(0,r.useState)([]),H=Z?(0,u.t)("Apply"):(0,u.t)("Save"),W=(0,m.Z)(),V=async e=>{const{error:t,statusText:i,message:r}=await(0,I.O$)(e);let l=t||i||(0,u.t)("An error has occurred");"object"===typeof r&&"json_metadata"in r?l=r.json_metadata:"string"===typeof r&&(l=r,"Forbidden"===r&&(l=(0,u.t)("You do not have permission to edit this dashboard"))),v.Z.error({title:(0,u.t)("Error"),content:l,okButtonProps:{danger:!0,className:"btn-danger"}})},Q=(0,r.useCallback)(((e="owners",t="",i,r)=>{const l=h().encode({filter:t,page:i,page_size:r});return g.Z.get({endpoint:`/api/v1/dashboard/related/${e}?q=${l}`}).then((e=>({data:e.json.result.filter((e=>void 0===e.extra.active||e.extra.active)).map((e=>({value:e.value,label:e.text}))),totalCount:e.json.count})))}),[]),Y=(0,r.useCallback)((e=>{const{id:t,dashboard_title:i,slug:r,certified_by:l,certification_details:a,owners:n,roles:o,metadata:d,is_managed_externally:c}=e,h={id:t,title:i,slug:r||"",certifiedBy:l||"",certificationDetails:a||"",isManagedExternally:c||!1};$.setFieldsValue(h),X(h),J(n),P(o),A(d.color_scheme),null!=d&&d.positions&&delete d.positions;const p={...d};delete p.shared_label_colors,delete p.color_scheme_domain,K(p?s()(p):"")}),[$]),G=(0,r.useCallback)((()=>{O(!0),g.Z.get({endpoint:`/api/v1/dashboard/${n}`}).then((e=>{var t;const i=e.json.result,r=null!=(t=i.json_metadata)&&t.length?JSON.parse(i.json_metadata):{};Y({...i,metadata:r}),O(!1)}),V)}),[n,Y]),ee=()=>{try{return null!=z&&z.length?JSON.parse(z):{}}catch(e){return{}}},te=e=>{const t=(0,f.Z)(e).map((e=>({id:e.value,full_name:e.label})));J(t)},ie=()=>(D||[]).map((e=>({value:e.id,label:e.full_name||`${e.first_name} ${e.last_name}`}))),re=(e="",{updateMetadata:t=!0}={})=>{const i=W.keys(),r=ee();if(e&&!i.includes(e))throw v.Z.error({title:(0,u.t)("Error"),content:(0,u.t)("A valid color scheme is required"),okButtonProps:{danger:!0,className:"btn-danger"}}),new Error("A valid color scheme is required");t&&(r.color_scheme=e,r.label_colors=r.label_colors||{},K(s()(r))),A(e)};return(0,r.useEffect)((()=>{S&&(c?Y(c):G()),F.Ad.preload()}),[c,G,Y,S]),(0,r.useEffect)((()=>{p&&L&&L.title!==p&&$.setFieldsValue({...L,title:p})}),[L,p,$]),(0,k.tZ)(v.Z,{show:S,onHide:x,title:(0,u.t)("Dashboard properties"),footer:(0,k.tZ)(r.Fragment,null,(0,k.tZ)(o.Z,{htmlType:"button",buttonSize:"small",onClick:x,"data-test":"properties-modal-cancel-button",cta:!0},(0,u.t)("Cancel")),(0,k.tZ)(o.Z,{"data-test":"properties-modal-apply-button",onClick:$.submit,buttonSize:"small",buttonStyle:"primary",className:"m-r-5",cta:!0,disabled:null==L?void 0:L.isManagedExternally,tooltip:null!=L&&L.isManagedExternally?(0,u.t)("This dashboard is managed externally, and can't be edited in Superset"):""},H)),responsive:!0},(0,k.tZ)(d.qz,{form:$,onFinish:()=>{var i,r,l,a;const{title:o,slug:d,certifiedBy:c,certificationDetails:h}=$.getFieldsValue();let p,m=j,f="",v=z;try{if(!v.startsWith("{")||!v.endsWith("}"))throw new Error;p=JSON.parse(v)}catch(e){return void t((0,u.t)("JSON metadata is invalid!"))}m=(null==(i=p)?void 0:i.color_scheme)||j,f=null==(r=p)?void 0:r.color_namespace,null!=(l=p)&&l.shared_label_colors&&delete p.shared_label_colors,null!=(a=p)&&a.color_scheme_domain&&delete p.color_scheme_domain;const F=(0,b.ZP)();var k;(y.getNamespace(f).resetColors(),m)?(F.updateColorMap(f,m),p.shared_label_colors=Object.fromEntries(F.getColorMap()),p.color_scheme_domain=(null==(k=W.get(j))?void 0:k.colors)||[]):(F.reset(),p.shared_label_colors={},p.color_scheme_domain=[]);v=s()(p),re(m,{updateMetadata:!1});const S={},w={};(0,U.cr)(E.T.DASHBOARD_RBAC)&&(S.roles=B,w.roles=(B||[]).map((e=>e.id)));const N={id:n,title:o,slug:d,jsonMetadata:v,owners:D,colorScheme:m,colorNamespace:f,certifiedBy:c,certificationDetails:h,...S};Z?(C(N),x(),e((0,u.t)("Dashboard properties updated"))):g.Z.put({endpoint:`/api/v1/dashboard/${n}`,headers:{"Content-Type":"application/json"},body:JSON.stringify({dashboard_title:o,slug:d||null,json_metadata:v||null,owners:(D||[]).map((e=>e.id)),certified_by:c||null,certification_details:c&&h?h:null,...w})}).then((()=>{C(N),x(),e((0,u.t)("The dashboard has been saved"))}),V)},"data-test":"dashboard-edit-properties-form",layout:"vertical",initialValues:L},(0,k.tZ)(d.X2,null,(0,k.tZ)(d.JX,{xs:24,md:24},(0,k.tZ)("h3",null,(0,u.t)("Basic information")))),(0,k.tZ)(d.X2,{gutter:16},(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)(a.xJ,{label:(0,u.t)("Title"),name:"title"},(0,k.tZ)(l.II,{"data-test":"dashboard-title-input",type:"text",disabled:w}))),(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)(R,{label:(0,u.t)("URL slug"),name:"slug"},(0,k.tZ)(l.II,{type:"text",disabled:w})),(0,k.tZ)("p",{className:"help-block"},(0,u.t)("A readable URL for your dashboard")))),(0,U.cr)(E.T.DASHBOARD_RBAC)?(()=>{const e=ee(),t=!!Object.keys((null==e?void 0:e.label_colors)||{}).length;return(0,k.tZ)(r.Fragment,null,(0,k.tZ)(d.X2,null,(0,k.tZ)(d.JX,{xs:24,md:24},(0,k.tZ)("h3",{style:{marginTop:"1em"}},(0,u.t)("Access")))),(0,k.tZ)(d.X2,{gutter:16},(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)(R,{label:(0,u.t)("Owners")},(0,k.tZ)(d.qb,{allowClear:!0,ariaLabel:(0,u.t)("Owners"),disabled:w,mode:"multiple",onChange:te,options:(e,t,i)=>Q("owners",e,t,i),value:ie()})),(0,k.tZ)("p",{className:"help-block"},(0,u.t)("Owners is a list of users who can alter the dashboard. Searchable by name or username.")))),(0,k.tZ)(d.X2,null,(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)(N,{hasCustomLabelColors:t,onChange:re,colorScheme:j,labelMargin:4}))))})():(()=>{const e=ee(),t=!!Object.keys((null==e?void 0:e.label_colors)||{}).length;return(0,k.tZ)(d.X2,{gutter:16},(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)("h3",{style:{marginTop:"1em"}},(0,u.t)("Access")),(0,k.tZ)(R,{label:(0,u.t)("Owners")},(0,k.tZ)(d.qb,{allowClear:!0,ariaLabel:(0,u.t)("Owners"),disabled:w,mode:"multiple",onChange:te,options:(e,t,i)=>Q("owners",e,t,i),value:ie()})),(0,k.tZ)("p",{className:"help-block"},(0,u.t)("Owners is a list of users who can alter the dashboard. Searchable by name or username."))),(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)("h3",{style:{marginTop:"1em"}},(0,u.t)("Colors")),(0,k.tZ)(N,{hasCustomLabelColors:t,onChange:re,colorScheme:j,labelMargin:4})))})(),(0,k.tZ)(d.X2,null,(0,k.tZ)(d.JX,{xs:24,md:24},(0,k.tZ)("h3",null,(0,u.t)("Certification")))),(0,k.tZ)(d.X2,{gutter:16},(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)(R,{label:(0,u.t)("Certified by"),name:"certifiedBy"},(0,k.tZ)(l.II,{type:"text",disabled:w})),(0,k.tZ)("p",{className:"help-block"},(0,u.t)("Person or group that has certified this dashboard."))),(0,k.tZ)(d.JX,{xs:24,md:12},(0,k.tZ)(R,{label:(0,u.t)("Certification details"),name:"certificationDetails"},(0,k.tZ)(l.II,{type:"text",disabled:w})),(0,k.tZ)("p",{className:"help-block"},(0,u.t)("Any additional detail to show in the certification tooltip.")))),(0,k.tZ)(d.X2,null,(0,k.tZ)(d.JX,{xs:24,md:24},(0,k.tZ)("h3",{style:{marginTop:"1em"}},(0,k.tZ)(o.Z,{buttonStyle:"link",onClick:()=>q(!M)},(0,k.tZ)("i",{className:"fa fa-angle-"+(M?"down":"right"),style:{minWidth:"1em"}}),(0,u.t)("Advanced"))),M&&(0,k.tZ)(r.Fragment,null,(0,k.tZ)(R,{label:(0,u.t)("JSON metadata")},(0,k.tZ)(T,{showLoadingForImport:!0,name:"json_metadata",value:z,onChange:K,tabSize:2,width:"100%",height:"200px",wrapEnabled:!0})),(0,k.tZ)("p",{className:"help-block"},(0,u.t)("This JSON object is generated dynamically when clicking the save or overwrite button in the dashboard view. It is exposed here for reference and for power users who may want to alter specific parameters."),Z&&(0,k.tZ)(r.Fragment,null," ",(0,u.t)('Please DO NOT overwrite the "filter_scopes" key.')," ",(0,k.tZ)(_.Z,{triggerNode:(0,k.tZ)("span",{className:"alert-link"},(0,u.t)('Use "%(menuName)s" menu instead.',{menuName:(0,u.t)("Set filter mapping")}))}))))))))}))},968084:(e,t,i)=>{i.d(t,{Z:()=>ge});var r=i(667294),l=i(751995),a=i(601304),n=i(828216),s=i(14890),o=i(781395),d=i(909467),c=i(45697),h=i.n(c),p=i(294184),u=i.n(p),m=i(835932),g=i(211965),f=i(455867),b=i(441609),y=i.n(b),v=i(680621),F=i(81255);const x=[F.gn,F.U0];function Z({currentNode:e={},components:t={},filterFields:i=[],selectedChartId:r}){if(!e)return null;const{type:l}=e;if(F.dW===l&&e&&e.meta&&e.meta.chartId){const t={value:e.meta.chartId,label:e.meta.sliceName||`${l} ${e.meta.chartId}`,type:l,showCheckbox:r!==e.meta.chartId};return{...t,children:i.map((i=>({value:`${e.meta.chartId}:${i}`,label:`${t.label}`,type:"filter_box",showCheckbox:!1})))}}let a=[];if(e.children&&e.children.length&&e.children.forEach((e=>{const l=Z({currentNode:t[e],components:t,filterFields:i,selectedChartId:r}),n=t[e].type;x.includes(n)?a.push(l):a=a.concat(l)})),x.includes(l)){let t=null;return t=l===F.U0?(0,f.t)("All charts"):e.meta&&e.meta.text?e.meta.text:`${l} ${e.id}`,{value:e.id,label:t,type:l,children:a}}return a}function C({components:e={},filterFields:t=[],selectedChartId:i}){if(y()(e))return[];return[{...Z({currentNode:e[v._4],components:e,filterFields:t,selectedChartId:i})}]}function k(e=[],t=-1){const i=[],r=(e,l)=>{e&&e.children&&(-1===t||l<t)&&(i.push(e.value),e.children.forEach((e=>r(e,l+1))))};return e.length>0&&e.forEach((e=>{r(e,0)})),i}var S=i(309679);function $({activeFilterField:e,checkedFilterFields:t}){return(0,S.o)(e?[e]:t)}var w=i(820194);function N({activeFilterField:e,checkedFilterFields:t}){if(e)return(0,w._)(e).chartId;if(t.length){const{chartId:e}=(0,w._)(t[0]);return t.some((t=>(0,w._)(t).chartId!==e))?null:e}return null}function _({checkedFilterFields:e=[],activeFilterField:t,filterScopeMap:i={},layout:r={}}){const l=$({checkedFilterFields:e,activeFilterField:t}),a=t?[t]:e,n=C({components:r,filterFields:a,selectedChartId:N({checkedFilterFields:e,activeFilterField:t})}),s=new Set;a.forEach((e=>{(i[e].checked||[]).forEach((t=>{s.add(`${t}:${e}`)}))}));const o=[...s],d=i[l]?i[l].expanded:k(n,1);return{[l]:{nodes:n,nodesFiltered:[...n],checked:o,expanded:d}}}var I=i(594654),O=i.n(I),U=i(283927),E=i.n(U),R=i(958809),T=i.n(R),M=i(108816),q=i.n(M);function j({tabScopes:e,parentNodeValue:t,forceAggregate:i=!1,hasChartSiblings:r=!1,tabChildren:l=[],immuneChartSiblings:a=[]}){if(i||!r&&Object.entries(e).every((([e,{scope:t}])=>t&&t.length&&e===t[0]))){const i=function({tabs:e=[],tabsInScope:t=[]}){const i=[];return e.forEach((({value:e,children:r})=>{r&&!t.includes(e)&&r.forEach((({value:e,children:r})=>{r&&!t.includes(e)&&i.push(...r.filter((({type:e})=>e===F.dW)))}))})),i.map((({value:e})=>e))}({tabs:l,tabsInScope:O()(e,(({scope:e})=>e))}),r=O()(Object.values(e),(({immune:e})=>e));return{scope:[t],immune:[...new Set([...i,...r])]}}const n=Object.values(e).filter((({scope:e})=>e&&e.length));return{scope:O()(n,(({scope:e})=>e)),immune:n.length?O()(n,(({immune:e})=>e)):O()(Object.values(e),(({immune:e})=>e)).concat(a)}}function A({currentNode:e={},filterId:t,checkedChartIds:i=[]}){if(!e)return{};const{value:r,children:l}=e,a=l.filter((({type:e})=>e===F.dW)),n=l.filter((({type:e})=>e===F.gn)),s=a.filter((({value:e})=>t!==e&&!i.includes(e))).map((({value:e})=>e)),o=q()(T()((e=>e.value)),E()((e=>A({currentNode:e,filterId:t,checkedChartIds:i}))))(n);if(!y()(a)&&a.some((({value:e})=>i.includes(e)))){if(y()(n))return{scope:[r],immune:s};const{scope:e,immune:t}=j({tabScopes:o,parentNodeValue:r,forceAggregate:!0,tabChildren:n});return{scope:e,immune:s.concat(t)}}return n.length?j({tabScopes:o,parentNodeValue:r,hasChartSiblings:!y()(a),tabChildren:n,immuneChartSiblings:s}):{scope:[],immune:s}}function z({filterKey:e,nodes:t=[],checkedChartIds:i=[]}){if(t.length){const{chartId:r}=(0,w._)(e);return A({currentNode:t[0],filterId:r,checkedChartIds:i})}return{}}var K=i(643399),L=i(602275),X=i(228388),D=i.n(X),J=i(731293);const B=(0,l.iK)(J.Z.BarChartOutlined)`
  ${({theme:e})=>`\n    position: relative;\n    top: ${e.gridUnit-1}px;\n    color: ${e.colors.primary.base};\n    margin-right: ${2*e.gridUnit}px;\n  `}
`;function P({currentNode:e={},selectedChartId:t}){if(!e)return null;const{label:i,value:r,type:l,children:a}=e;if(a&&a.length){const n=a.map((e=>P({currentNode:e,selectedChartId:t})));return{...e,label:(0,g.tZ)("span",{className:u()(`filter-scope-type ${l.toLowerCase()}`,{"selected-filter":t===r})},l===F.dW&&(0,g.tZ)(B,null),i),children:n}}return{...e,label:(0,g.tZ)("span",{className:u()(`filter-scope-type ${l.toLowerCase()}`,{"selected-filter":t===r})},i)}}function H({nodes:e,selectedChartId:t}){return e?e.map((e=>P({currentNode:e,selectedChartId:t}))):[]}var W=i(513842);const V={check:(0,g.tZ)(W.lU,null),uncheck:(0,g.tZ)(W.zq,null),halfCheck:(0,g.tZ)(W.dc,null),expandClose:(0,g.tZ)("span",{className:"rct-icon rct-icon-expand-close"}),expandOpen:(0,g.tZ)("span",{className:"rct-icon rct-icon-expand-open"}),expandAll:(0,g.tZ)("span",{className:"rct-icon rct-icon-expand-all"},(0,f.t)("Expand all")),collapseAll:(0,g.tZ)("span",{className:"rct-icon rct-icon-collapse-all"},(0,f.t)("Collapse all")),parentClose:(0,g.tZ)("span",{className:"rct-icon rct-icon-parent-close"}),parentOpen:(0,g.tZ)("span",{className:"rct-icon rct-icon-parent-open"}),leaf:(0,g.tZ)("span",{className:"rct-icon rct-icon-leaf"})},Q={nodes:h().arrayOf(L.ck).isRequired,checked:h().arrayOf(h().oneOfType([h().number,h().string])).isRequired,expanded:h().arrayOf(h().oneOfType([h().number,h().string])).isRequired,onCheck:h().func.isRequired,onExpand:h().func.isRequired,selectedChartId:h().number},Y=()=>{};function G({nodes:e=[],checked:t=[],expanded:i=[],onCheck:r,onExpand:l,selectedChartId:a}){return(0,g.tZ)(D(),{showExpandAll:!0,expandOnClick:!0,showNodeIcon:!1,nodes:H({nodes:e,selectedChartId:a}),checked:t,expanded:i,onCheck:r,onExpand:l,onClick:Y,icons:V})}G.propTypes=Q,G.defaultProps={selectedChartId:null};var ee=i(49238);const te={label:h().string.isRequired,isSelected:h().bool.isRequired};function ie({label:e,isSelected:t}){return(0,g.tZ)("span",{className:u()("filter-field-item filter-container",{"is-selected":t})},(0,g.tZ)(ee.lX,{htmlFor:e},e))}function re({nodes:e,activeKey:t}){if(!e)return[];const i=e[0],r=i.children.map((e=>({...e,children:e.children.map((e=>{const{label:i,value:r}=e;return{...e,label:(0,g.tZ)(ie,{isSelected:r===t,label:i})}}))})));return[{...i,label:(0,g.tZ)("span",{className:"root"},i.label),children:r}]}ie.propTypes=te;const le={activeKey:h().string,nodes:h().arrayOf(L.ck).isRequired,checked:h().arrayOf(h().oneOfType([h().number,h().string])).isRequired,expanded:h().arrayOf(h().oneOfType([h().number,h().string])).isRequired,onCheck:h().func.isRequired,onExpand:h().func.isRequired,onClick:h().func.isRequired};function ae({activeKey:e,nodes:t=[],checked:i=[],expanded:r=[],onClick:l,onCheck:a,onExpand:n}){return(0,g.tZ)(D(),{showExpandAll:!0,showNodeIcon:!1,expandOnClick:!0,nodes:re({nodes:t,activeKey:e}),checked:i,expanded:r,onClick:l,onCheck:a,onExpand:n,icons:V})}ae.propTypes=le,ae.defaultProps={activeKey:null};const ne={dashboardFilters:h().objectOf(L.Er).isRequired,layout:h().object.isRequired,updateDashboardFiltersScope:h().func.isRequired,setUnsavedChanges:h().func.isRequired,onCloseModal:h().func.isRequired},se=l.iK.div`
  ${({theme:e})=>g.iv`
    display: flex;
    flex-direction: column;
    height: 80%;
    margin-right: ${-6*e.gridUnit}px;
    font-size: ${e.typography.sizes.m}px;

    & .nav.nav-tabs {
      border: none;
    }

    & .filter-scope-body {
      flex: 1;
      max-height: calc(100% - ${32*e.gridUnit}px);

      .filter-field-pane,
      .filter-scope-pane {
        overflow-y: auto;
      }
    }

    & .warning-message {
      padding: ${6*e.gridUnit}px;
    }
  `}
`,oe=l.iK.div`
  ${({theme:e})=>g.iv`
    &.filter-scope-body {
      flex: 1;
      max-height: calc(100% - ${32*e.gridUnit}px);

      .filter-field-pane,
      .filter-scope-pane {
        overflow-y: auto;
      }
    }
  `}
`,de=l.iK.div`
  ${({theme:e})=>g.iv`
    height: ${16*e.gridUnit}px;
    border-bottom: 1px solid ${e.colors.grayscale.light2};
    padding-left: ${6*e.gridUnit}px;
    margin-left: ${-6*e.gridUnit}px;

    h4 {
      margin-top: 0;
    }

    .selected-fields {
      margin: ${3*e.gridUnit}px 0 ${4*e.gridUnit}px;
      visibility: hidden;

      &.multi-edit-mode {
        visibility: visible;
      }

      .selected-scopes {
        padding-left: ${e.gridUnit}px;
      }
    }
  `}
`,ce=l.iK.div`
  ${({theme:e})=>g.iv`
    &.filters-scope-selector {
      display: flex;
      flex-direction: row;
      position: relative;
      height: 100%;

      a,
      a:active,
      a:hover {
        color: inherit;
        text-decoration: none;
      }

      .react-checkbox-tree .rct-icon.rct-icon-expand-all,
      .react-checkbox-tree .rct-icon.rct-icon-collapse-all {
        font-family: ${e.typography.families.sansSerif};
        font-size: ${e.typography.sizes.m}px;
        color: ${e.colors.primary.base};

        &::before {
          content: '';
        }

        &:hover {
          text-decoration: underline;
        }

        &:focus {
          outline: none;
        }
      }

      .filter-field-pane {
        position: relative;
        width: 40%;
        padding: ${4*e.gridUnit}px;
        padding-left: 0;
        border-right: 1px solid ${e.colors.grayscale.light2};

        .filter-container label {
          font-weight: ${e.typography.weights.normal};
          margin: 0 0 0 ${4*e.gridUnit}px;
          word-break: break-all;
        }

        .filter-field-item {
          height: ${9*e.gridUnit}px;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 0 ${6*e.gridUnit}px;
          margin-left: ${-6*e.gridUnit}px;

          &.is-selected {
            border: 1px solid ${e.colors.text.label};
            border-radius: ${e.borderRadius}px;
            background-color: ${e.colors.grayscale.light4};
            margin-left: ${-6*e.gridUnit}px;
          }
        }

        .react-checkbox-tree {
          .rct-title .root {
            font-weight: ${e.typography.weights.bold};
          }

          .rct-text {
            height: ${10*e.gridUnit}px;
          }
        }
      }

      .filter-scope-pane {
        position: relative;
        flex: 1;
        padding: ${4*e.gridUnit}px;
        padding-right: ${6*e.gridUnit}px;
      }

      .react-checkbox-tree {
        flex-direction: column;
        color: ${e.colors.grayscale.dark1};
        font-size: ${e.typography.sizes.m}px;

        .filter-scope-type {
          padding: ${2*e.gridUnit}px 0;
          display: flex;
          align-items: center;

          &.chart {
            font-weight: ${e.typography.weights.normal};
          }

          &.selected-filter {
            padding-left: ${7*e.gridUnit}px;
            position: relative;
            color: ${e.colors.text.label};

            &::before {
              content: ' ';
              position: absolute;
              left: 0;
              top: 50%;
              width: ${4*e.gridUnit}px;
              height: ${4*e.gridUnit}px;
              border-radius: ${e.borderRadius}px;
              margin-top: ${-2*e.gridUnit}px;
              box-shadow: inset 0 0 0 2px ${e.colors.grayscale.light2};
              background: ${e.colors.grayscale.light3};
            }
          }

          &.root {
            font-weight: ${e.typography.weights.bold};
          }
        }

        .rct-checkbox {
          svg {
            position: relative;
            top: 3px;
            width: ${4.5*e.gridUnit}px;
          }
        }

        .rct-node-leaf {
          .rct-bare-label {
            &::before {
              padding-left: ${e.gridUnit}px;
            }
          }
        }

        .rct-options {
          text-align: left;
          margin-left: 0;
          margin-bottom: ${2*e.gridUnit}px;
        }

        .rct-text {
          margin: 0;
          display: flex;
        }

        .rct-title {
          display: block;
        }

        // disable style from react-checkbox-trees.css
        .rct-node-clickable:hover,
        .rct-node-clickable:focus,
        label:hover,
        label:active {
          background: none !important;
        }
      }

      .multi-edit-mode {
        &.filter-scope-pane {
          .rct-node.rct-node-leaf .filter-scope-type.filter_box {
            display: none;
          }
        }

        .filter-field-item {
          padding: 0 ${4*e.gridUnit}px 0 ${12*e.gridUnit}px;
          margin-left: ${-12*e.gridUnit}px;

          &.is-selected {
            margin-left: ${-13*e.gridUnit}px;
          }
        }
      }

      .scope-search {
        position: absolute;
        right: ${4*e.gridUnit}px;
        top: ${4*e.gridUnit}px;
        border-radius: ${e.borderRadius}px;
        border: 1px solid ${e.colors.grayscale.light2};
        padding: ${e.gridUnit}px ${2*e.gridUnit}px;
        font-size: ${e.typography.sizes.m}px;
        outline: none;

        &:focus {
          border: 1px solid ${e.colors.primary.base};
        }
      }
    }
  `}
`,he=l.iK.div`
  ${({theme:e})=>`\n    height: ${16*e.gridUnit}px;\n\n    border-top: ${e.gridUnit/4}px solid ${e.colors.primary.light3};\n    padding: ${6*e.gridUnit}px;\n    margin: 0 0 0 ${6*-e.gridUnit}px;\n    text-align: right;\n\n    .btn {\n      margin-right: ${4*e.gridUnit}px;\n\n      &:last-child {\n        margin-right: 0;\n      }\n    }\n  `}
`;class pe extends r.PureComponent{constructor(e){super(e);const{dashboardFilters:t,layout:i}=e;if(Object.keys(t).length>0){const e=function({dashboardFilters:e={}}){const t=Object.values(e).map((e=>{const{chartId:t,filterName:i,columns:r,labels:l}=e,a=Object.keys(r).map((e=>({value:(0,w.w)({chartId:t,column:e}),label:l[e]||e})));return{value:t,label:i,children:a,showCheckbox:!0}}));return[{value:v.dU,type:F.U0,label:(0,f.t)("All filters"),children:t}]}({dashboardFilters:t}),r=e[0].children;this.allfilterFields=[],r.forEach((({children:e})=>{e.forEach((e=>{this.allfilterFields.push(e.value)}))})),this.defaultFilterKey=r[0].children[0].value;const l=Object.values(t).reduce(((e,{chartId:r,columns:l})=>({...e,...Object.keys(l).reduce(((e,l)=>{const a=(0,w.w)({chartId:r,column:l}),n=C({components:i,filterFields:[a],selectedChartId:r}),s=k(n,1),o=((0,K.up)({filterScope:t[r].scopes[l]})||[]).filter((e=>e!==r));return{...e,[a]:{nodes:n,nodesFiltered:[...n],checked:o,expanded:s}}}),{})})),{}),{chartId:a}=(0,w._)(this.defaultFilterKey),n=[],s=this.defaultFilterKey,o=[v.dU].concat(a),d=_({checkedFilterFields:n,activeFilterField:s,filterScopeMap:l,layout:i});this.state={showSelector:!0,activeFilterField:s,searchText:"",filterScopeMap:{...l,...d},filterFieldNodes:e,checkedFilterFields:n,expandedFilterIds:o}}else this.state={showSelector:!1};this.filterNodes=this.filterNodes.bind(this),this.onChangeFilterField=this.onChangeFilterField.bind(this),this.onCheckFilterScope=this.onCheckFilterScope.bind(this),this.onExpandFilterScope=this.onExpandFilterScope.bind(this),this.onSearchInputChange=this.onSearchInputChange.bind(this),this.onCheckFilterField=this.onCheckFilterField.bind(this),this.onExpandFilterField=this.onExpandFilterField.bind(this),this.onClose=this.onClose.bind(this),this.onSave=this.onSave.bind(this)}onCheckFilterScope(e=[]){const{activeFilterField:t,filterScopeMap:i,checkedFilterFields:r}=this.state,l=$({activeFilterField:t,checkedFilterFields:r}),a=t?[t]:r,n={...i[l],checked:e},s=function({checked:e=[],filterFields:t=[],filterScopeMap:i={}}){const r=e.reduce(((e,t)=>{const[i,r]=t.split(":");return{...e,[r]:(e[r]||[]).concat(parseInt(i,10))}}),{});return t.reduce(((e,t)=>{const{chartId:l}=(0,w._)(t),a=(r[t]||[]).filter((e=>e!==l));return{...e,[t]:{...i[t],checked:a}}}),{})}({checked:e,filterFields:a,filterScopeMap:i});this.setState((()=>({filterScopeMap:{...i,...s,[l]:n}})))}onExpandFilterScope(e=[]){const{activeFilterField:t,checkedFilterFields:i,filterScopeMap:r}=this.state,l=$({activeFilterField:t,checkedFilterFields:i}),a={...r[l],expanded:e};this.setState((()=>({filterScopeMap:{...r,[l]:a}})))}onCheckFilterField(e=[]){const{layout:t}=this.props,{filterScopeMap:i}=this.state,r=_({checkedFilterFields:e,activeFilterField:null,filterScopeMap:i,layout:t});this.setState((()=>({activeFilterField:null,checkedFilterFields:e,filterScopeMap:{...i,...r}})))}onExpandFilterField(e=[]){this.setState((()=>({expandedFilterIds:e})))}onChangeFilterField(e={}){const{layout:t}=this.props,i=e.value,{activeFilterField:r,checkedFilterFields:l,filterScopeMap:a}=this.state;if(i===r){const e=_({checkedFilterFields:l,activeFilterField:null,filterScopeMap:a,layout:t});this.setState({activeFilterField:null,filterScopeMap:{...a,...e}})}else if(this.allfilterFields.includes(i)){const e=_({checkedFilterFields:l,activeFilterField:i,filterScopeMap:a,layout:t});this.setState({activeFilterField:i,filterScopeMap:{...a,...e}})}}onSearchInputChange(e){this.setState({searchText:e.target.value},this.filterTree)}onClose(){this.props.onCloseModal()}onSave(){const{filterScopeMap:e}=this.state,t=this.allfilterFields.reduce(((t,i)=>{const{nodes:r}=e[i],l=e[i].checked;return{...t,[i]:z({filterKey:i,nodes:r,checkedChartIds:l})}}),{});this.props.updateDashboardFiltersScope(t),this.props.setUnsavedChanges(!0),this.props.onCloseModal()}filterTree(){if(this.state.searchText){const e=e=>{const{activeFilterField:t,checkedFilterFields:i,filterScopeMap:r}=e,l=$({activeFilterField:t,checkedFilterFields:i}),a=r[l].nodes.reduce(this.filterNodes,[]),n=k([...a]),s={...r[l],nodesFiltered:a,expanded:n};return{filterScopeMap:{...r,[l]:s}}};this.setState(e)}else this.setState((e=>{const{activeFilterField:t,checkedFilterFields:i,filterScopeMap:r}=e,l=$({activeFilterField:t,checkedFilterFields:i}),a={...r[l],nodesFiltered:r[l].nodes};return{filterScopeMap:{...r,[l]:a}}}))}filterNodes(e=[],t={}){const{searchText:i}=this.state,r=(t.children||[]).reduce(this.filterNodes,[]);return(t.label.toLocaleLowerCase().indexOf(i.toLocaleLowerCase())>-1||r.length)&&e.push({...t,children:r}),e}renderFilterFieldList(){const{activeFilterField:e,filterFieldNodes:t,checkedFilterFields:i,expandedFilterIds:r}=this.state;return(0,g.tZ)(ae,{activeKey:e,nodes:t,checked:i,expanded:r,onClick:this.onChangeFilterField,onCheck:this.onCheckFilterField,onExpand:this.onExpandFilterField})}renderFilterScopeTree(){const{filterScopeMap:e,activeFilterField:t,checkedFilterFields:i,searchText:l}=this.state,a=$({activeFilterField:t,checkedFilterFields:i}),n=N({activeFilterField:t,checkedFilterFields:i});return(0,g.tZ)(r.Fragment,null,(0,g.tZ)("input",{className:"filter-text scope-search multi-edit-mode",placeholder:(0,f.t)("Search..."),type:"text",value:l,onChange:this.onSearchInputChange}),(0,g.tZ)(G,{nodes:e[a].nodesFiltered,checked:e[a].checked,expanded:e[a].expanded,onCheck:this.onCheckFilterScope,onExpand:this.onExpandFilterScope,selectedChartId:n}))}renderEditingFiltersName(){const{dashboardFilters:e}=this.props,{activeFilterField:t,checkedFilterFields:i}=this.state,r=[].concat(t||i).map((t=>{const{chartId:i,column:r}=(0,w._)(t);return e[i].labels[r]||r}));return(0,g.tZ)("div",{className:"selected-fields multi-edit-mode"},0===r.length&&(0,f.t)("No filter is selected."),1===r.length&&(0,f.t)("Editing 1 filter:"),r.length>1&&(0,f.t)("Batch editing %d filters:",r.length),(0,g.tZ)("span",{className:"selected-scopes"},r.join(", ")))}render(){const{showSelector:e}=this.state;return(0,g.tZ)(se,null,(0,g.tZ)(de,null,(0,g.tZ)("h4",null,(0,f.t)("Configure filter scopes")),e&&this.renderEditingFiltersName()),(0,g.tZ)(oe,{className:"filter-scope-body"},e?(0,g.tZ)(ce,{className:"filters-scope-selector"},(0,g.tZ)("div",{className:u()("filter-field-pane multi-edit-mode")},this.renderFilterFieldList()),(0,g.tZ)("div",{className:"filter-scope-pane multi-edit-mode"},this.renderFilterScopeTree())):(0,g.tZ)("div",{className:"warning-message"},(0,f.t)("There are no filters in this dashboard."))),(0,g.tZ)(he,null,(0,g.tZ)(m.Z,{buttonSize:"small",onClick:this.onClose},(0,f.t)("Close")),e&&(0,g.tZ)(m.Z,{buttonSize:"small",buttonStyle:"primary",onClick:this.onSave},(0,f.t)("Save"))))}}pe.propTypes=ne;const ue=(0,n.$j)((function({dashboardLayout:e,dashboardFilters:t}){return{dashboardFilters:t,layout:e.present}}),(function(e){return(0,s.DE)({updateDashboardFiltersScope:o.l6,setUnsavedChanges:d.if},e)}))(pe),me=l.iK.div((({theme:{gridUnit:e}})=>({padding:2*e,paddingBottom:3*e})));class ge extends r.PureComponent{constructor(e){super(e),this.modal=void 0,this.modal=r.createRef(),this.handleCloseModal=this.handleCloseModal.bind(this)}handleCloseModal(){var e,t;null==this||null==(e=this.modal)||null==(t=e.current)||null==t.close||t.close()}render(){const e={onCloseModal:this.handleCloseModal};return(0,g.tZ)(a.Z,{ref:this.modal,triggerNode:this.props.triggerNode,modalBody:(0,g.tZ)(me,null,(0,g.tZ)(ue,e)),width:"80%"})}}},400713:(e,t,i)=>{i.d(t,{Z:()=>a});var r=i(455867),l=i(680621);const a=[{value:l.HE,label:(0,r.t)("Transparent"),className:"background--transparent"},{value:l.b5,label:(0,r.t)("White"),className:"background--white"}]},879271:(e,t,i)=>{i.d(t,{Z:()=>a});var r=i(455867),l=i(680621);const a=[{value:l.u_,label:(0,r.t)("Small"),className:"header-style-option header-small"},{value:l.OE,label:(0,r.t)("Medium"),className:"header-style-option header-medium"},{value:l.pQ,label:(0,r.t)("Large"),className:"header-style-option header-large"}]}}]);