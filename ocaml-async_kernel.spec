#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Monadic concurrency library
Summary(pl.UTF-8):	Biblioteka współbieżności monadowej
Name:		ocaml-async_kernel
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/async_kernel/tags
Source0:	https://github.com/janestreet/async_kernel/archive/v%{version}/async_kernel-%{version}.tar.gz
# Source0-md5:	3ccd1dc3bb50601fc84ce66b31989282
URL:		https://github.com/janestreet/async_kernel
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-core_kernel-devel >= 0.14
BuildRequires:	ocaml-core_kernel-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Async_kernel contains Async's core data structures, like Deferred.
Async_kernel is portable, and so can be used in JavaScript using
Async_js.

This package contains files needed to run bytecode executables using
async_kernel library.

%description -l pl.UTF-8
Async_kernel zawiera podstawowe struktury danych modułu Async, takie
jak Deferred. Async_kernel jest przenośna, więc może być używana z
poziomu JavaScriptu przy użyciu Async_js.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki async_kernel.

%package devel
Summary:	Monadic concurrency library - development part
Summary(pl.UTF-8):	Biblioteka współbieżności monadowej - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-core_kernel-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
async_kernel library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki async_kernel.

%prep
%setup -q -n async_kernel-%{version}

%build
dune build --release --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/async_kernel/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/async_kernel/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/async_kernel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/async_kernel
%{_libdir}/ocaml/async_kernel/META
%{_libdir}/ocaml/async_kernel/*.cma
%dir %{_libdir}/ocaml/async_kernel/eager_deferred
%{_libdir}/ocaml/async_kernel/eager_deferred/*.cma
%dir %{_libdir}/ocaml/async_kernel/limiter_async
%{_libdir}/ocaml/async_kernel/limiter_async/*.cma
%dir %{_libdir}/ocaml/async_kernel/persistent_connection_kernel
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cma
%dir %{_libdir}/ocaml/async_kernel/weak_hashtbl_async
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/async_kernel/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/async_kernel/eager_deferred/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/async_kernel/limiter_async/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/async_kernel/*.cmi
%{_libdir}/ocaml/async_kernel/*.cmt
%{_libdir}/ocaml/async_kernel/*.cmti
%{_libdir}/ocaml/async_kernel/*.mli
%{_libdir}/ocaml/async_kernel/eager_deferred/*.cmi
%{_libdir}/ocaml/async_kernel/eager_deferred/*.cmt
%{_libdir}/ocaml/async_kernel/eager_deferred/*.cmti
%{_libdir}/ocaml/async_kernel/eager_deferred/*.mli
%{_libdir}/ocaml/async_kernel/limiter_async/*.cmi
%{_libdir}/ocaml/async_kernel/limiter_async/*.cmt
%{_libdir}/ocaml/async_kernel/limiter_async/*.cmti
%{_libdir}/ocaml/async_kernel/limiter_async/*.mli
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cmi
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cmt
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cmti
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.mli
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cmi
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cmt
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cmti
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/async_kernel/async_kernel.a
%{_libdir}/ocaml/async_kernel/*.cmx
%{_libdir}/ocaml/async_kernel/*.cmxa
%{_libdir}/ocaml/async_kernel/eager_deferred/eager_deferred.a
%{_libdir}/ocaml/async_kernel/eager_deferred/*.cmx
%{_libdir}/ocaml/async_kernel/eager_deferred/*.cmxa
%{_libdir}/ocaml/async_kernel/limiter_async/limiter_async.a
%{_libdir}/ocaml/async_kernel/limiter_async/*.cmx
%{_libdir}/ocaml/async_kernel/limiter_async/*.cmxa
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/persistent_connection_kernel.a
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cmx
%{_libdir}/ocaml/async_kernel/persistent_connection_kernel/*.cmxa
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/weak_hashtbl_async.a
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cmx
%{_libdir}/ocaml/async_kernel/weak_hashtbl_async/*.cmxa
%endif
%{_libdir}/ocaml/async_kernel/dune-package
%{_libdir}/ocaml/async_kernel/opam
